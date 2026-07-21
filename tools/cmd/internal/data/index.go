package data

import (
	"sort"
	"strings"
	"sync"

	"github.com/cmd4coder/cmd4coder/internal/model"
	"github.com/sahilm/fuzzy"
)

type Index struct {
	nameIndex     map[string]*model.Command
	categoryIndex map[string][]*model.Command
	keywordIndex  map[string][]*model.Command
	platformIndex map[string][]*model.Command

	mu sync.RWMutex
}

func NewIndex() *Index {
	return &Index{
		nameIndex:     make(map[string]*model.Command),
		categoryIndex: make(map[string][]*model.Command),
		keywordIndex:  make(map[string][]*model.Command),
		platformIndex: make(map[string][]*model.Command),
	}
}

type commandSearchData struct {
	nameLower     string
	nameSlice     []string
	descSlice     []string
	categorySlice []string
}

var searchDataCache sync.Map

func getSearchData(cmd *model.Command) *commandSearchData {
	if v, ok := searchDataCache.Load(cmd); ok {
		return v.(*commandSearchData)
	}
	sd := &commandSearchData{
		nameLower:     strings.ToLower(cmd.Name),
		nameSlice:     []string{cmd.Name},
		descSlice:     []string{cmd.Description},
		categorySlice: []string{cmd.Category},
	}
	searchDataCache.Store(cmd, sd)
	return sd
}

func (idx *Index) BuildIndex(commands []*model.Command) error {
	idx.mu.Lock()
	defer idx.mu.Unlock()

	searchDataCache.Range(func(key, _ interface{}) bool {
		searchDataCache.Delete(key)
		return true
	})

	idx.nameIndex = make(map[string]*model.Command)
	idx.categoryIndex = make(map[string][]*model.Command)
	idx.keywordIndex = make(map[string][]*model.Command)
	idx.platformIndex = make(map[string][]*model.Command)

	for _, cmd := range commands {
		if _, exists := idx.nameIndex[cmd.Name]; exists {
			return model.ErrDuplicateCommand{Name: cmd.Name}
		}

		idx.nameIndex[cmd.Name] = cmd

		idx.categoryIndex[cmd.Category] = append(idx.categoryIndex[cmd.Category], cmd)

		for _, platform := range cmd.Platforms {
			idx.platformIndex[platform] = append(idx.platformIndex[platform], cmd)
		}

		idx.buildKeywordIndex(cmd)
	}

	return nil
}

func (idx *Index) buildKeywordIndex(cmd *model.Command) {
	keywords := make(map[string]bool)

	for _, word := range tokenize(cmd.Name) {
		keywords[word] = true
	}

	for _, word := range tokenize(cmd.Description) {
		keywords[word] = true
	}

	for _, word := range tokenize(cmd.Category) {
		keywords[word] = true
	}

	for keyword := range keywords {
		idx.keywordIndex[keyword] = append(idx.keywordIndex[keyword], cmd)
	}
}

var cjkDict = map[string]bool{
	"控制平面": true, "访问控制": true, "准入策略": true, "签名请求": true,
	"签名请求批准": true, "证书管理": true, "密钥管理": true, "模板验证": true,
	"模板测试": true, "仓库成员": true, "仓库权限": true, "配置管理": true,
	"基础设施": true, "查看状态": true, "限制范围": true, "命令行": true,
	"数据库": true, "容器化": true, "命名空间": true, "证书签名": true,
	"证书签名请求": true, "命名": true, "已安装": true,
	"工具": true, "管理": true, "配置": true, "查询": true,
	"搜索": true, "部署": true, "构建": true, "容器": true, "网络": true,
	"诊断": true, "监控": true, "安全": true, "镜像": true, "集群": true,
	"存储": true, "日志": true, "策略": true, "运行": true, "编排": true,
	"节点": true, "服务": true, "网格": true, "内存": true, "磁盘": true,
	"组件": true, "模型": true, "训练": true, "推理": true, "计划": true,
	"任务": true, "数据": true, "引擎": true, "指标": true, "审计": true,
	"资源": true, "配额": true, "基线": true, "标准": true, "范围": true,
	"列表": true, "授权": true, "拉取": true, "推送": true, "删除": true,
	"描述": true, "状态": true, "创建": true, "更新": true, "补丁": true,
	"应用": true, "证书": true, "密钥": true, "模板": true, "仓库": true,
	"添加": true, "设置": true, "清理": true, "压缩": true, "解压": true,
	"列出": true, "上传": true, "下载": true, "安装": true, "卸载": true,
	"版本": true, "初始化": true, "生成": true, "测试": true, "停止": true,
	"提交": true, "分支": true, "合并": true, "变基": true, "重置": true,
	"检出": true, "差异": true, "标签": true, "远程": true, "克隆": true,
	"切换": true, "验证": true, "批准": true, "成员": true, "权限": true,
	"文件": true, "目录": true, "进程": true, "用户": true,
	"防火墙": true, "路由": true, "负载": true, "均衡": true,
	"缓存": true, "消息": true, "队列": true, "管道": true, "流水线": true,
	"接口": true, "协议": true, "端口": true, "域名": true,
	"回滚": true, "扩容": true, "缩容": true, "迁移": true, "备份": true,
	"恢复": true, "分析": true, "追踪": true,
	"链路": true, "采样": true, "阈值": true, "告警": true, "通知": true,
	"报表": true, "仪表盘": true, "面板": true, "插件": true, "扩展": true,
	"模块": true, "包": true, "依赖": true, "注册": true, "发现": true,
	"代理": true, "网关": true, "中间件": true, "过滤": true, "转发": true,
	"重试": true, "超时": true, "熔断": true, "降级": true, "限流": true,
	"分片": true, "副本": true, "主从": true, "读写": true, "分离": true,
	"事务": true, "索引": true, "分区": true, "快照": true, "归档": true,
	"导入": true, "导出": true, "同步": true, "异步": true, "并发": true,
	"协程": true, "线程": true, "锁": true, "信号": true, "事件": true,
	"回调": true, "钩子": true, "装饰": true, "适配": true,
	"绑定": true, "序列化": true, "反序列化": true, "编码": true, "解码": true,
	"加密": true, "解密": true, "哈希": true, "签名": true, "令牌": true,
	"身份": true, "认证": true, "鉴权": true, "角色": true, "组": true,
	"空间": true, "隔离": true, "限制": true, "优先级": true,
	"调度": true, "亲和": true, "污点": true, "容忍": true, "守护": true,
	"工作": true, "定时": true, "周期": true, "触发": true, "条件": true,
	"规则": true, "模式": true, "匹配": true, "替换": true, "转换": true,
	"映射": true, "解析": true, "格式": true, "类型": true, "结构": true,
	"定义": true, "声明": true, "引用": true, "注入": true, "环境": true,
	"变量": true, "参数": true, "选项": true, "标志": true, "子命令": true,
	"帮助": true, "示例": true, "文档": true, "说明": true, "用法": true,
	"输出": true, "输入": true, "重定向": true, "连接": true,
	"断开": true, "监听": true, "请求": true, "响应": true,
	"头信息": true, "体": true, "方法": true, "路径": true,
	"主体": true, "状态码": true, "错误": true, "异常": true,
	"警告": true, "信息": true, "详细": true, "静默": true,
	"交互": true, "批量": true, "并行": true, "串行": true, "递归": true,
	"迭代": true, "循环": true, "判断": true, "逻辑": true,
	"算术": true, "比较": true, "运算": true, "处理": true, "计算": true,
	"统计": true, "汇总": true, "聚合": true, "分组": true, "排序": true,
	"去重": true, "分页": true, "偏移": true,
	"游标": true, "窗口": true, "视图": true, "物化": true, "临时": true,
	"全局": true, "局部": true, "常量": true, "静态": true, "动态": true,
	"单例": true, "工厂": true, "建造": true, "原型": true, "外观": true,
	"享元": true, "责任链": true, "命令": true, "迭代器": true,
	"观察者": true, "模板方法": true, "访问者": true,
	"健康": true, "检查": true, "探针": true, "存活": true, "就绪": true,
	"启动": true, "终止": true, "优雅": true, "强制": true,
	"滚动": true, "蓝绿": true, "金丝雀": true, "灰度": true, "预发": true,
	"生产": true, "开发": true, "预生产": true, "沙箱": true,
	"虚拟机": true, "裸金属": true, "混合云": true, "私有云": true,
	"公有云": true, "多云": true, "边缘": true, "联邦": true, "多集群": true,
	"灾备": true, "高可用": true, "弹性": true, "伸缩": true, "自动": true,
	"手动": true, "半自动": true, "无人值守": true, "持续集成": true,
	"持续交付": true, "持续部署": true, "基础设施即代码": true,
}

var cjkMaxLen = 7

func init() {
	for w := range cjkDict {
		runes := []rune(w)
		if len(runes) > cjkMaxLen {
			cjkMaxLen = len(runes)
		}
	}
}

func isCJK(r rune) bool {
	return (r >= 0x4e00 && r <= 0x9fff) || (r >= 0x3400 && r <= 0x4dbf) || (r >= 0xf900 && r <= 0xfaff)
}

func hasCJK(s string) bool {
	for _, r := range s {
		if isCJK(r) {
			return true
		}
	}
	return false
}

func segmentCJK(text string) []string {
	runes := []rune(text)
	if len(runes) == 0 {
		return nil
	}

	var result []string
	i := 0
	for i < len(runes) {
		if !isCJK(runes[i]) {
			start := i
			for i < len(runes) && !isCJK(runes[i]) {
				i++
			}
			word := string(runes[start:i])
			if len([]rune(word)) > 1 {
				result = append(result, word)
			}
			continue
		}

		maxLen := cjkMaxLen
		if i+maxLen > len(runes) {
			maxLen = len(runes) - i
		}

		matched := false
		for length := maxLen; length >= 2; length-- {
			candidate := string(runes[i : i+length])
			if cjkDict[candidate] {
				result = append(result, candidate)
				i += length
				matched = true
				break
			}
		}

		if !matched {
			if i+1 < len(runes) && isCJK(runes[i+1]) {
				result = append(result, string(runes[i:i+2]))
				i += 2
			} else {
				result = append(result, string(runes[i]))
				i++
			}
		}
	}

	return result
}

func tokenize(text string) []string {
	text = strings.ToLower(text)
	text = strings.ReplaceAll(text, "/", " ")
	text = strings.ReplaceAll(text, "_", " ")
	text = strings.ReplaceAll(text, "-", " ")

	words := strings.Fields(text)
	var result []string
	for _, word := range words {
		if hasCJK(word) {
			segments := segmentCJK(word)
			for _, seg := range segments {
				r := []rune(seg)
				if len(r) > 1 {
					result = append(result, seg)
				}
			}
		} else if len(word) > 1 {
			result = append(result, word)
		}
	}
	return result
}

func (idx *Index) GetByName(name string) (*model.Command, error) {
	idx.mu.RLock()
	defer idx.mu.RUnlock()

	cmd, ok := idx.nameIndex[name]
	if !ok {
		return nil, model.ErrCommandNotFound{Name: name}
	}
	return cmd, nil
}

func (idx *Index) GetByCategory(category string) []*model.Command {
	idx.mu.RLock()
	defer idx.mu.RUnlock()
	if result, ok := idx.categoryIndex[category]; ok {
		return result
	}
	return []*model.Command{}
}

func (idx *Index) GetByPlatform(platform string) []*model.Command {
	idx.mu.RLock()
	defer idx.mu.RUnlock()
	if result, ok := idx.platformIndex[platform]; ok {
		return result
	}
	return []*model.Command{}
}

func (idx *Index) GetAllCategories() []string {
	idx.mu.RLock()
	defer idx.mu.RUnlock()

	categories := make([]string, 0, len(idx.categoryIndex))
	for category := range idx.categoryIndex {
		categories = append(categories, category)
	}
	return categories
}

func (idx *Index) GetAllCommands() []*model.Command {
	idx.mu.RLock()
	defer idx.mu.RUnlock()

	commands := make([]*model.Command, 0, len(idx.nameIndex))
	for _, cmd := range idx.nameIndex {
		commands = append(commands, cmd)
	}
	return commands
}

func (idx *Index) CountCommands() int {
	idx.mu.RLock()
	defer idx.mu.RUnlock()
	return len(idx.nameIndex)
}

func (idx *Index) CountCategories() int {
	idx.mu.RLock()
	defer idx.mu.RUnlock()
	return len(idx.categoryIndex)
}

func (idx *Index) GetAllCommandNames() []string {
	idx.mu.RLock()
	defer idx.mu.RUnlock()

	names := make([]string, 0, len(idx.nameIndex))
	for name := range idx.nameIndex {
		names = append(names, name)
	}
	return names
}

type searchResult struct {
	command          *model.Command
	priority         int
	matchedPositions []int
}

func sortSearchResults(results []*searchResult) {
	sort.Slice(results, func(i, j int) bool {
		if results[i].priority != results[j].priority {
			return results[i].priority > results[j].priority
		}
		return results[i].command.Name < results[j].command.Name
	})
}

func (idx *Index) Search(query string, maxResults int) []*model.Command {
	idx.mu.RLock()
	defer idx.mu.RUnlock()

	query = strings.TrimSpace(query)
	if query == "" {
		return nil
	}

	words := strings.Fields(query)
	if len(words) == 0 {
		return nil
	}

	accumulated := make(map[string]*searchResult)

	for _, cmd := range idx.nameIndex {
		allMatch := true
		totalScore := 0
		combinedPositions := make(map[int]bool)

		for _, word := range words {
			word = strings.ToLower(word)
			score, positions := idx.scoreCommandWord(cmd, word)
			if score <= 0 {
				allMatch = false
				break
			}
			totalScore += score
			for _, p := range positions {
				combinedPositions[p] = true
			}
		}

		if !allMatch {
			continue
		}

		posSlice := make([]int, 0, len(combinedPositions))
		for p := range combinedPositions {
			posSlice = append(posSlice, p)
		}
		sort.Ints(posSlice)

		accumulated[cmd.Name] = &searchResult{
			command:          cmd,
			priority:         totalScore,
			matchedPositions: posSlice,
		}
	}

	var results []*searchResult
	for _, r := range accumulated {
		results = append(results, r)
	}

	sortSearchResults(results)

	if maxResults > 0 && len(results) > maxResults {
		results = results[:maxResults]
	}

	commands := make([]*model.Command, len(results))
	for i, r := range results {
		commands[i] = r.command
	}

	return commands
}

func (idx *Index) scoreCommandWord(cmd *model.Command, word string) (int, []int) {
	sd := getSearchData(cmd)

	if sd.nameLower == word {
		positions := make([]int, len(cmd.Name))
		for i := range positions {
			positions[i] = i
		}
		return 200, positions
	}

	if nameMatches := fuzzy.Find(word, sd.nameSlice); len(nameMatches) > 0 {
		score := 150 + nameMatches[0].Score/20
		return score, nameMatches[0].MatchedIndexes
	}

	if strings.HasPrefix(sd.nameLower, word) {
		positions := make([]int, len(word))
		for i := range positions {
			positions[i] = i
		}
		return 120, positions
	}

	if strings.Contains(sd.nameLower, word) {
		startIdx := strings.Index(sd.nameLower, word)
		positions := make([]int, len(word))
		for i := range positions {
			positions[i] = startIdx + i
		}
		return 100, positions
	}

	if len(fuzzy.Find(word, sd.descSlice)) > 0 {
		return 70, nil
	}

	if len(fuzzy.Find(word, sd.categorySlice)) > 0 {
		return 50, nil
	}

	if idx.keywordIndex[word] != nil {
		for _, c := range idx.keywordIndex[word] {
			if c.Name == cmd.Name {
				return 40, nil
			}
		}
	}

	return 0, nil
}

func (idx *Index) SuggestCommand(name string) string {
	idx.mu.RLock()
	defer idx.mu.RUnlock()

	if name == "" {
		return ""
	}

	allNames := make([]string, 0, len(idx.nameIndex))
	for n := range idx.nameIndex {
		allNames = append(allNames, n)
	}

	results := fuzzy.Find(name, allNames)
	if len(results) == 0 {
		return ""
	}

	return results[0].Str
}
