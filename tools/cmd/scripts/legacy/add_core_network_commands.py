#!/usr/bin/env python3
"""
补齐 Linux 核心系统/网络命令与网络基础设施命令。
"""
import sys
from pathlib import Path
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True
yaml.default_flow_style = False

DATA_DIR = Path("data")
META_PATH = DATA_DIR / "metadata.yaml"


def opt(flag_desc: str) -> dict:
    parts = flag_desc.split(" ", 1)
    return {"flag": parts[0], "description": parts[1] if len(parts) > 1 else ""}


def ex(cmd: str, desc: str) -> dict:
    return {"command": cmd, "description": desc}


def make_cmd(
    name: str,
    desc: str,
    category: str,
    usage: str = None,
    options: list = None,
    examples: list = None,
    related: list = None,
    install_required: bool = False,
    install_method: str = None,
    platforms: list = None,
    risk: str = "low",
    risk_desc: str = None,
) -> dict:
    if usage is None:
        usage = f"{name} [OPTIONS] [ARGS]"
    if options is None:
        options = ["--help 显示帮助信息", "--version 显示版本信息"]
    if examples is None:
        examples = [[f"{name} --help", "查看帮助"], [f"{name} --version", "查看版本"]]
    if platforms is None:
        platforms = ["linux", "darwin"]
    if related is None:
        related = []
    cmd = {
        "name": name,
        "category": category,
        "install_required": install_required,
        "description": desc,
        "usage": [usage],
        "options": [opt(o) for o in options],
        "examples": [ex(e[0], e[1]) for e in examples],
        "platforms": platforms,
        "related_commands": related,
    }
    if install_required and install_method:
        cmd["install_method"] = install_method
    if risk in ("medium", "high", "critical"):
        if risk_desc is None:
            risk_desc = "操作前请确认参数、目标环境和影响范围，建议在测试环境先行验证。"
        cmd["risks"] = [{"level": risk, "description": risk_desc}]
    return cmd


BATCH = {
    "os/linux-core.yaml": {
        "category": "操作系统/Linux核心",
        "description": "Linux 系统、网络、存储、硬件等核心底层命令",
        "commands": [
            make_cmd("ip", "Linux 网络配置与路由管理核心工具", "操作系统/Linux核心",
                     usage="ip [OPTIONS] OBJECT {COMMAND}",
                     options=["-s 显示统计", "-4 仅 IPv4", "-6 仅 IPv6", "-br 简要输出"],
                     examples=[["ip addr show", "显示网卡地址"], ["sudo ip route add default via 192.168.1.1", "添加默认路由"]],
                     related=["iptables", "nmcli", "ss"], risk="high", risk_desc="修改地址、路由或链路状态可能导致网络中断，远程操作时尤其危险"),
            make_cmd("iptables", "IPv4 包过滤与 NAT 防火墙", "操作系统/Linux核心",
                     usage="iptables [OPTIONS] -t table -A chain rule",
                     options=["-A 追加规则", "-D 删除规则", "-L 列出规则", "-F 清空规则"],
                     examples=[["sudo iptables -L -v -n", "列出当前规则"], ["sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT", "允许 SSH"]],
                     related=["nftables", "ip", "ufw"], risk="high", risk_desc="错误的规则会阻断合法流量或放行攻击，修改前请保存并测试"),
            make_cmd("nftables", "新一代 nftables 防火墙（nft 命令）", "操作系统/Linux核心",
                     usage="nft [OPTIONS] COMMAND",
                     options=["list ruleset 列出规则", "add table 创建表", "add chain 创建链", "add rule 添加规则"],
                     examples=[["sudo nft list ruleset", "列出所有规则"], ["sudo nft add table ip filter", "创建 filter 表"]],
                     related=["iptables", "ip"], risk="high", risk_desc="nftables 规则直接影响网络策略，请在本地测试后再应用"),
            make_cmd("tc", "Linux 流量控制（Traffic Control）", "操作系统/Linux核心",
                     usage="tc [OPTIONS] qdisc|class|filter ...",
                     options=["show 显示配置", "add 添加 qdisc", "change 修改", "del 删除"],
                     examples=[["tc qdisc show", "显示当前 qdisc"], ["sudo tc qdisc add dev eth0 root netem delay 100ms", "模拟 100ms 延迟"]],
                     related=["iptables", "ip"], risk="high", risk_desc="流量控制会改变网络延迟和带宽，生产环境请谨慎"),
            make_cmd("ipset", "IP 集合管理，常与 iptables 配合", "操作系统/Linux核心",
                     usage="ipset [OPTIONS] COMMAND",
                     options=["create 创建集合", "add 添加成员", "del 删除成员", "list 列出"],
                     examples=[["sudo ipset create blacklist hash:ip", "创建 IP 黑名单集合"], ["sudo ipset add blacklist 1.2.3.4", "添加 IP"]],
                     related=["iptables", "nftables"], risk="medium", risk_desc="误删或误加 IP 会影响防火墙策略，请确认集合用途"),
            make_cmd("bridge", "以太网桥管理", "操作系统/Linux核心",
                     usage="bridge [OPTIONS] OBJECT {COMMAND}",
                     options=["link show 显示桥接端口", "fdb show 显示转发数据库", "vlan show 显示 VLAN"],
                     examples=[["bridge link show", "显示桥接接口"], ["bridge fdb show", "显示 MAC 转发表"]],
                     related=["ip", "nmcli"], risk="medium", risk_desc="桥接配置错误会导致二层网络异常"),
            make_cmd("netplan", "Ubuntu 网络配置管理工具", "操作系统/Linux核心",
                     usage="netplan [OPTIONS] COMMAND",
                     options=["generate 生成配置", "apply 应用配置", "try 试用配置", "info 显示信息"],
                     examples=[["sudo netplan generate", "生成网络配置"], ["sudo netplan apply", "应用网络配置"]],
                     related=["nmcli", "ip"], risk="high", risk_desc="netplan apply 会立即修改网络，远程服务器请先用 netplan try"),
            make_cmd("nmcli", "NetworkManager 命令行工具", "操作系统/Linux核心",
                     usage="nmcli [OPTIONS] OBJECT {COMMAND}",
                     options=["device status 设备状态", "connection up 启用连接", "connection show 查看连接"],
                     examples=[["nmcli device status", "查看网卡状态"], ["nmcli connection up 'Wired connection 1'", "启用指定连接"]],
                     related=["nmtui", "ip", "netplan"], risk="medium", risk_desc="关闭或切换连接会中断网络，远程操作需谨慎"),
            make_cmd("resolvectl", "systemd-resolved DNS 解析控制", "操作系统/Linux核心",
                     usage="resolvectl [OPTIONS] COMMAND",
                     options=["query 解析域名", "status 查看状态", "flush-caches 清空缓存"],
                     examples=[["resolvectl query example.com", "查询域名"], ["resolvectl flush-caches", "清空 DNS 缓存"]],
                     related=["dig", "systemd-resolve"], risk="low"),
            make_cmd("dmesg", "查看内核环形缓冲区消息", "操作系统/Linux核心",
                     options=["-T 人类可读时间", "-l 按级别过滤", "-w 实时跟踪", "-n 设置日志级别"],
                     examples=[["dmesg -T", "查看带时间戳的内核日志"], ["dmesg -w", "实时跟踪内核日志"]],
                     related=["journalctl", "sysctl"], risk="low"),
            make_cmd("lscpu", "显示 CPU 架构与信息", "操作系统/Linux核心",
                     options=["-e 表格输出", "-p 解析格式", "-a 在线与离线 CPU"],
                     examples=[["lscpu", "显示 CPU 信息"], ["lscpu -e", "表格显示每个 CPU"]],
                     related=["lspci", "lsusb"], risk="low"),
            make_cmd("lspci", "列出 PCI 设备", "操作系统/Linux核心",
                     options=["-v 详细", "-k 显示内核驱动", "-nn 显示厂商 ID"],
                     examples=[["lspci", "列出 PCI 设备"], ["lspci -k | grep -A3 Ethernet", "查看网卡驱动"]],
                     related=["lsusb", "lscpu"], risk="low"),
            make_cmd("lsusb", "列出 USB 设备", "操作系统/Linux核心",
                     options=["-v 详细", "-t 树状", "-s 指定总线/设备"],
                     examples=[["lsusb", "列出 USB 设备"], ["lsusb -v -d 046d:", "查看罗技设备详情"]],
                     related=["lspci", "dmesg"], risk="low"),
            make_cmd("lsmem", "列出内存信息", "操作系统/Linux核心",
                     options=["-a 所有内存", "-o 指定输出列", "-b 以字节显示"],
                     examples=[["lsmem", "显示内存布局"], ["lsmem -a", "显示所有内存信息"]],
                     related=["free", "lscpu"], risk="low"),
            make_cmd("dmidecode", "从 DMI 表读取硬件信息", "操作系统/Linux核心",
                     usage="dmidecode [OPTIONS]",
                     options=["-t 指定类型", "-s 指定字符串关键字", "-q 安静模式"],
                     examples=[["sudo dmidecode -t memory", "查看内存信息"], ["sudo dmidecode -s system-serial-number", "查看序列号"]],
                     related=["lscpu", "lspci"], risk="low"),
            make_cmd("sysctl", "运行时内核参数管理", "操作系统/Linux核心",
                     usage="sysctl [OPTIONS] [VARIABLE[=VALUE]...]",
                     options=["-a 列出所有参数", "-w 临时写入", "-p 从文件加载", "-n 只输出值"],
                     examples=[["sysctl -a | grep ipv4.ip_forward", "查看 IP 转发设置"], ["sudo sysctl -w net.ipv4.ip_forward=1", "临时开启 IP 转发"]],
                     related=["systemctl", "dmesg"], risk="high", risk_desc="错误的内核参数可能导致系统不稳定或网络异常，修改前请了解含义"),
            make_cmd("fsck", "检查并修复文件系统", "操作系统/Linux核心",
                     usage="fsck [OPTIONS] DEVICE",
                     options=["-y 自动回答 yes", "-n 只检查不修复", "-t 指定文件系统类型"],
                     examples=[["sudo fsck -n /dev/sda1", "只检查不修复"], ["sudo fsck -y /dev/sda1", "自动修复错误"]],
                     related=["mkfs", "tune2fs"], risk="critical", risk_desc="fsck 会修改文件系统结构，操作前请卸载分区并备份"),
            make_cmd("mkfs", "创建文件系统", "操作系统/Linux核心",
                     usage="mkfs [OPTIONS] [-t TYPE] DEVICE",
                     options=["-t 指定类型", "-L 设置卷标", "-V 详细输出"],
                     examples=[["sudo mkfs -t ext4 /dev/sdb1", "格式化为 ext4"], ["sudo mkfs.xfs -L data /dev/sdc1", "格式化为 XFS 并设置卷标"]],
                     related=["fsck", "parted"], risk="critical", risk_desc="mkfs 会清除设备上所有数据，请确认目标分区正确"),
            make_cmd("tune2fs", "调整 ext2/3/4 文件系统参数", "操作系统/Linux核心",
                     usage="tune2fs [OPTIONS] DEVICE",
                     options=["-l 列出超级块信息", "-L 设置卷标", "-m 保留块百分比"],
                     examples=[["sudo tune2fs -l /dev/sda1", "查看文件系统信息"], ["sudo tune2fs -L rootfs /dev/sda1", "设置卷标"]],
                     related=["mkfs", "fsck"], risk="high", risk_desc="tune2fs 修改文件系统元数据，请确认参数并备份"),
            make_cmd("pvcreate", "初始化物理卷（LVM）", "操作系统/Linux核心",
                     usage="pvcreate [OPTIONS] DEVICE",
                     options=["-f 强制", "-y 自动 yes", "--dataalignment 对齐"],
                     examples=[["sudo pvcreate /dev/sdb", "将磁盘初始化为物理卷"], ["sudo pvcreate -f /dev/sdc1", "强制初始化"]],
                     related=["vgcreate", "lvcreate"], risk="critical", risk_desc="pvcreate 会覆盖设备上的分区信息，请确认无重要数据"),
            make_cmd("vgcreate", "创建卷组（LVM）", "操作系统/Linux核心",
                     usage="vgcreate [OPTIONS] VOLUME_GROUP PHYSICAL_VOLUME...",
                     options=["-s 指定物理扩展大小", "-v 详细输出"],
                     examples=[["sudo vgcreate vg0 /dev/sdb /dev/sdc", "创建卷组 vg0"], ["sudo vgcreate -s 16M vg1 /dev/sdd", "指定 PE 大小"]],
                     related=["pvcreate", "lvcreate"], risk="high", risk_desc="创建卷组会占用物理卷，请确认目标设备"),
            make_cmd("lvcreate", "创建逻辑卷（LVM）", "操作系统/Linux核心",
                     usage="lvcreate [OPTIONS] -n NAME -L SIZE VOLUME_GROUP",
                     options=["-n 逻辑卷名", "-L 指定大小", "-l 指定 LE 数", "-s 创建快照"],
                     examples=[["sudo lvcreate -n lv0 -L 100G vg0", "在 vg0 上创建 100G 逻辑卷"], ["sudo lvcreate -s -n snap -L 10G /dev/vg0/lv0", "创建快照"]],
                     related=["vgcreate", "pvcreate"], risk="high", risk_desc="逻辑卷操作影响存储布局，请确认大小和卷组"),
            make_cmd("lvs", "显示逻辑卷信息（LVM）", "操作系统/Linux核心",
                     options=["-a 所有", "-o 指定输出列", "-v 详细"],
                     examples=[["sudo lvs", "列出逻辑卷"], ["sudo lvs -o +devices", "显示底层设备"]],
                     related=["vgs", "pvs"], risk="low"),
            make_cmd("vgs", "显示卷组信息（LVM）", "操作系统/Linux核心",
                     options=["-v 详细", "-o 指定输出列"],
                     examples=[["sudo vgs", "列出卷组"], ["sudo vgs -o vg_name,vg_size,vg_free", "显示卷组大小与空闲"]],
                     related=["lvs", "pvs"], risk="low"),
            make_cmd("pvs", "显示物理卷信息（LVM）", "操作系统/Linux核心",
                     options=["-v 详细", "-o 指定输出列"],
                     examples=[["sudo pvs", "列出物理卷"], ["sudo pvs -o pv_name,vg_name,pv_size", "显示物理卷与所属卷组"]],
                     related=["lvs", "vgs"], risk="low"),
            make_cmd("cryptsetup", "LUKS/dm-crypt 磁盘加密工具", "操作系统/Linux核心",
                     usage="cryptsetup [OPTIONS] COMMAND [ARGS]",
                     options=["luksFormat 格式化", "open 打开", "close 关闭", "status 状态"],
                     examples=[["sudo cryptsetup luksFormat /dev/sdb1", "创建 LUKS 加密分区"], ["sudo cryptsetup open /dev/sdb1 secret", "打开加密映射"]],
                     related=["mkfs", "mount"], risk="critical", risk_desc="luksFormat 会擦除数据并加密，丢失密钥将导致数据永久不可恢复"),
            make_cmd("hdparm", "查看和设置 SATA/IDE 硬盘参数", "操作系统/Linux核心",
                     usage="hdparm [OPTIONS] [DEVICE]",
                     options=["-I 显示详细信息", "-t 缓存读测速", "-T 缓存读测速", "-y 进入待机"],
                     examples=[["sudo hdparm -I /dev/sda", "查看硬盘信息"], ["sudo hdparm -tT /dev/sda", "测速"]],
                     related=["smartctl", "lsblk"], risk="medium", risk_desc="设置电源管理或安全擦除参数可能影响硬盘寿命或数据"),
            make_cmd("less", "分页查看文件内容", "操作系统/Linux核心",
                     usage="less [OPTIONS] FILE",
                     options=["-N 显示行号", "-S 不换行", "+F 实时跟踪", "-i 忽略大小写"],
                     examples=[["less /var/log/syslog", "查看日志"], ["less +F /var/log/app.log", "实时跟踪日志"]],
                     related=["more", "cat"], risk="low"),
            make_cmd("more", "简单分页查看文件", "操作系统/Linux核心",
                     usage="more [OPTIONS] FILE",
                     options=["-num 每页行数", "+num 从指定行开始"],
                     examples=[["more /var/log/syslog", "分页查看日志"], ["more +100 file.txt", "从第 100 行开始"]],
                     related=["less", "cat"], risk="low"),
            make_cmd("man", "查看命令/函数手册页", "操作系统/Linux核心",
                     usage="man [OPTIONS] [SECTION] NAME",
                     options=["-k 关键字搜索", "-f 同 whatis", "-a 显示所有匹配节"],
                     examples=[["man ls", "查看 ls 手册"], ["man 5 passwd", "查看配置文件格式"]],
                     related=["info", "whatis"], risk="low"),
            make_cmd("which", "查找命令可执行文件路径", "操作系统/Linux核心",
                     usage="which [OPTIONS] COMMAND",
                     options=["-a 显示所有匹配", "--skip-alias 跳过别名"],
                     examples=[["which python3", "查找 python3 路径"], ["which -a node", "显示所有 node 路径"]],
                     related=["whereis", "type"], risk="low"),
            make_cmd("whereis", "查找命令二进制/源码/手册位置", "操作系统/Linux核心",
                     usage="whereis [OPTIONS] COMMAND",
                     options=["-b 只找二进制", "-m 只找手册", "-s 只找源码"],
                     examples=[["whereis python3", "查找 python3 相关文件"], ["whereis -b gcc", "只找 gcc 二进制"]],
                     related=["which", "man"], risk="low"),
            make_cmd("whatis", "显示命令简短描述", "操作系统/Linux核心",
                     usage="whatis [OPTIONS] KEYWORD",
                     options=["-r 正则匹配", "-w 精确匹配"],
                     examples=[["whatis ls", "显示 ls 简介"], ["whatis -w passwd", "精确匹配"]],
                     related=["man", "apropos"], risk="low"),
            make_cmd("apropos", "按关键字搜索手册页", "操作系统/Linux核心",
                     usage="apropos [OPTIONS] KEYWORD",
                     options=["-r 正则", "-e 精确匹配", "-s 指定节"],
                     examples=[["apropos network", "搜索网络相关命令"], ["apropos -s 1 copy", "在第 1 节搜索 copy"]],
                     related=["whatis", "man"], risk="low"),
            make_cmd("anacron", "用于非 24x7 机器执行周期性任务", "操作系统/Linux核心",
                     usage="anacron [OPTIONS]",
                     options=["-f 立即执行", "-n 忽略延迟", "-T 测试 anacrontab"],
                     examples=[["sudo anacron -f", "立即运行 anacron 任务"], ["sudo anacron -T", "检查配置文件语法"]],
                     related=["crontab", "at"], risk="medium", risk_desc="anacron 任务会按系统启动时间补跑，脚本错误可能集中产生副作用"),
            make_cmd("sha256sum", "计算或校验 SHA-256 校验和", "操作系统/Linux核心",
                     usage="sha256sum [OPTIONS] [FILE]",
                     options=["-c 校验", "-b 二进制模式", "--tag BSD 风格"],
                     examples=[["sha256sum file.iso > file.iso.sha256", "生成校验文件"], ["sha256sum -c file.iso.sha256", "校验文件"]],
                     related=["md5sum", "cksum"], risk="low"),
            make_cmd("md5sum", "计算或校验 MD5 校验和", "操作系统/Linux核心",
                     usage="md5sum [OPTIONS] [FILE]",
                     options=["-c 校验", "--quiet 只显示错误"],
                     examples=[["md5sum file.txt", "计算 MD5"], ["md5sum -c checksum.md5", "校验 MD5"]],
                     related=["sha256sum", "cksum"], risk="low"),
            make_cmd("xxd", "十六进制查看器和编辑器", "操作系统/Linux核心",
                     usage="xxd [OPTIONS] [FILE]",
                     options=["-l 限制长度", "-s 跳过偏移", "-p 纯十六进制", "-r 反向转换"],
                     examples=[["xxd file.bin | head", "查看二进制文件"], ["xxd -p file.bin", "输出纯十六进制"]],
                     related=["od", "hexdump"], risk="low"),
            make_cmd("file", "识别文件类型", "操作系统/Linux核心",
                     usage="file [OPTIONS] FILE",
                     options=["-b 不显示文件名", "-i 显示 MIME 类型", "-L 跟随符号链接"],
                     examples=[["file /bin/ls", "识别文件类型"], ["file -i image.png", "显示 MIME 类型"]],
                     related=["xxd", "ls"], risk="low"),
            make_cmd("getent", "查询系统数据库条目", "操作系统/Linux核心",
                     usage="getent [OPTIONS] DATABASE [KEY]",
                     options=["passwd 用户", "group 组", "hosts 主机", "services 服务"],
                     examples=[["getent passwd root", "查询 root 用户信息"], ["getent hosts example.com", "查询主机名解析"]],
                     related=["id", "hostname"], risk="low"),
            make_cmd("iconv", "字符编码转换", "操作系统/Linux核心",
                     usage="iconv [OPTIONS] -f FROM -t TO [INPUT]",
                     options=["-f 源编码", "-t 目标编码", "-o 输出文件", "-l 列出编码"],
                     examples=[["iconv -f GBK -t UTF-8 input.txt > output.txt", "GBK 转 UTF-8"], ["iconv -l | grep -i gb", "列出含 GB 的编码"]],
                     related=["file", "enca"], risk="low"),
        ],
    },
    "network/infra.yaml": {
        "category": "网络工具/基础设施",
        "description": "反向代理、Web 服务器、VPN、DNS 服务等网络基础设施命令",
        "commands": [
            make_cmd("nginx", "高性能 Web 服务器与反向代理", "网络工具/基础设施",
                     usage="nginx [OPTIONS]",
                     options=["-t 测试配置", "-s signal 发送信号", "-c 指定配置文件", "-g 全局指令"],
                     examples=[["sudo nginx -t", "测试配置文件"], ["sudo nginx -s reload", "平滑重载配置"]],
                     related=["haproxy", "traefik", "caddy"], risk="medium", risk_desc="reload 失败或配置错误会中断服务，请先在测试环境验证"),
            make_cmd("haproxy", "TCP/HTTP 负载均衡器", "网络工具/基础设施",
                     usage="haproxy [OPTIONS]",
                     options=["-c 检查配置", "-f 配置文件", "-sf 平滑切换"],
                     examples=[["haproxy -c -f /etc/haproxy/haproxy.cfg", "检查配置"], ["sudo haproxy -f /etc/haproxy/haproxy.cfg", "启动 haproxy"]],
                     related=["nginx", "traefik"], risk="medium", risk_desc="负载均衡配置错误会导致流量异常，修改后请检查"),
            make_cmd("traefik", "云原生边缘路由/反向代理", "网络工具/基础设施",
                     usage="traefik [OPTIONS]",
                     options=["--configFile 配置文件", "--api.insecure", "--providers.docker"],
                     examples=[["traefik --configFile=traefik.toml", "加载配置文件启动"], ["traefik --providers.docker=true --api.insecure=true", "Docker 提供器模式"]],
                     related=["nginx", "caddy"], risk="medium", risk_desc="错误的 TLS 或路由配置会导致证书或服务不可达"),
            make_cmd("caddy", "易用且默认 HTTPS 的 Web 服务器", "网络工具/基础设施",
                     usage="caddy [COMMAND] [OPTIONS]",
                     options=["run 启动", "reverse-proxy 快速反向代理", "file-server 静态文件"],
                     examples=[["caddy run", "启动 Caddy"], ["caddy reverse-proxy --from :80 --to localhost:8080", "快速反向代理"]],
                     related=["nginx", "traefik"], risk="medium", risk_desc="Caddy 会自动申请证书，请确认域名解析和防火墙"),
            make_cmd("openvpn", "SSL/TLS VPN 解决方案", "网络工具/基础设施",
                     usage="openvpn [OPTIONS]",
                     options=["--config 配置文件", "--daemon 后台运行", "--client 客户端模式"],
                     examples=[["sudo openvpn --config client.ovpn", "使用配置文件连接 VPN"], ["sudo openvpn --daemon --config server.conf", "后台启动服务端"]],
                     related=["wg", "ipsec"], risk="medium", risk_desc="VPN 配置错误会将流量导向错误网络，请确认路由和证书"),
            make_cmd("wg", "WireGuard 快速、现代、安全的 VPN", "网络工具/基础设施",
                     usage="wg [OPTIONS] [COMMAND]",
                     options=["show 显示接口", "set 设置接口", "genkey 生成私钥", "pubkey 生成公钥"],
                     examples=[["wg genkey | tee privatekey | wg pubkey > publickey", "生成密钥对"], ["sudo wg show", "显示 WireGuard 接口"]],
                     related=["openvpn", "ip"], risk="medium", risk_desc="私钥泄露会导致 VPN 被攻破，请安全存储"),
            make_cmd("sshuttle", "基于 SSH 的透明代理 VPN", "网络工具/基础设施",
                     usage="sshuttle [OPTIONS] [USER@]HOST [SUBNETS]",
                     options=["-r 远程 SSH 主机", "-v 详细", "--dns 代理 DNS"],
                     examples=[["sshuttle -r user@jump 192.168.0.0/16", "通过跳板访问内网"], ["sshuttle -r user@jump 0/0 --dns", "全局代理并转发 DNS"]],
                     related=["ssh", "proxychains"], risk="medium", risk_desc="sshuttle 会改变系统路由，请确认目标子网和 DNS 配置"),
            make_cmd("named-checkconf", "检查 BIND DNS 配置文件语法", "网络工具/基础设施",
                     usage="named-checkconf [OPTIONS] [FILE]",
                     options=["-z 检查所有 zone", "-p 打印配置", "-t 指定 chroot"],
                     examples=[["sudo named-checkconf", "检查 named.conf"], ["sudo named-checkconf -z", "检查所有 zone"]],
                     related=["rndc", "dnsmasq"], risk="low"),
            make_cmd("rndc", "BIND DNS 服务器远程控制", "网络工具/基础设施",
                     usage="rndc [OPTIONS] COMMAND",
                     options=["reload 重载", "status 状态", "flush 清空缓存", "stop 停止"],
                     examples=[["sudo rndc reload", "重载 BIND"], ["sudo rndc status", "查看状态"]],
                     related=["named-checkconf", "nsupdate"], risk="medium", risk_desc="rndc stop/reload 会影响 DNS 服务，请在维护窗口执行"),
            make_cmd("nsupdate", "动态更新 DNS 记录", "网络工具/基础设施",
                     usage="nsupdate [OPTIONS] [FILE]",
                     options=["-k 密钥文件", "-v 详细", "-d 调试"],
                     examples=[["nsupdate -k Kexample.+157+12345.key", "使用 TSIG 密钥更新"], ["echo -e 'update add host.example.com 300 A 1.2.3.4\nsend' | nsupdate", "添加 A 记录"]],
                     related=["rndc", "dig"], risk="high", risk_desc="nsupdate 会修改 DNS 记录，错误的更新会影响域名解析"),
            make_cmd("dnsmasq", "轻量级 DNS 转发与 DHCP 服务器", "网络工具/基础设施",
                     usage="dnsmasq [OPTIONS]",
                     options=["--test 测试配置", "--no-daemon 前台运行", "--server 上游 DNS"],
                     examples=[["dnsmasq --test", "检查配置"], ["dnsmasq --no-daemon --log-queries", "前台运行并记录查询"]],
                     related=["unbound", "systemd-resolved"], risk="medium", risk_desc="dnsmasq 作为 DNS/DHCP 服务，错误配置会导致网络解析异常"),
            make_cmd("unbound-control", "Unbound DNS 服务器远程控制", "网络工具/基础设施",
                     usage="unbound-control [OPTIONS] COMMAND",
                     options=["status 状态", "reload 重载", "lookup 查询", "flush 清空缓存"],
                     examples=[["sudo unbound-control status", "查看 Unbound 状态"], ["sudo unbound-control flush example.com", "清空指定域名缓存"]],
                     related=["dnsmasq", "resolvectl"], risk="medium", risk_desc="重载或 flush 会影响 DNS 解析，请确认影响范围"),
            make_cmd("ifconfig", "传统网络接口配置工具", "网络工具/基础设施",
                     usage="ifconfig [INTERFACE] [OPTIONS]",
                     options=["up 启用", "down 禁用", "inet 设置 IP", "netmask 设置掩码"],
                     examples=[["ifconfig", "显示接口信息"], ["sudo ifconfig eth0 192.168.1.10 netmask 255.255.255.0", "配置 IP"]],
                     related=["ip", "route"], risk="medium", risk_desc="修改 IP 或关闭接口会中断网络，远程操作时请谨慎"),
            make_cmd("route", "传统路由表管理", "网络工具/基础设施",
                     usage="route [OPTIONS] COMMAND",
                     options=["add 添加路由", "del 删除路由", "-n 数字显示"],
                     examples=[["route -n", "显示路由表"], ["sudo route add -net 10.0.0.0/8 gw 192.168.1.1", "添加静态路由"]],
                     related=["ip", "ifconfig"], risk="high", risk_desc="错误路由可能导致网络不可达，远程服务器请通过带外管理操作"),
            make_cmd("netstat", "网络连接、路由、接口统计", "网络工具/基础设施",
                     usage="netstat [OPTIONS]",
                     options=["-t TCP", "-u UDP", "-l 监听", "-n 数字", "-p 显示进程"],
                     examples=[["netstat -tlnp", "显示监听端口和进程"], ["netstat -s", "显示协议统计"]],
                     related=["ss", "lsof"], risk="low"),
        ],
    },
}


def main() -> int:
    meta = yaml.load(open(META_PATH, "r", encoding="utf-8"))
    existing_names = set()
    for rel_file in meta["data_files"]:
        path = DATA_DIR / rel_file
        if not path.exists():
            continue
        doc = yaml.load(open(path, "r", encoding="utf-8"))
        for cmd in doc.get("commands", []):
            existing_names.add(cmd["name"])

    total_added = 0
    for rel_file, spec in BATCH.items():
        path = DATA_DIR / rel_file
        path.parent.mkdir(parents=True, exist_ok=True)
        commands = []
        skipped = []
        for cmd in spec["commands"]:
            if cmd["name"] in existing_names:
                skipped.append(cmd["name"])
                continue
            commands.append(cmd)
            existing_names.add(cmd["name"])
        if not commands:
            print(f"{rel_file}: all commands already exist, skipped")
            continue
        doc = {"category": spec["category"], "description": spec["description"], "commands": commands}
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(doc, f)
        cat_id = rel_file.replace("/", "_").replace("-", "_").replace(".", "_")
        meta["categories"][cat_id] = {
            "id": cat_id,
            "name": spec["category"],
            "description": spec["description"],
            "parent": "",
            "order": 250,
        }
        if rel_file not in meta["data_files"]:
            meta["data_files"].append(rel_file)
        print(f"{rel_file}: added {len(commands)}, skipped {len(skipped)}")
        total_added += len(commands)

    cmd_count = 0
    for rel_file in meta["data_files"]:
        doc = yaml.load(open(DATA_DIR / rel_file, "r", encoding="utf-8"))
        cmd_count += len(doc["commands"])
    meta["description"] = f"cmd4coder 命令行工具大全数据文件 - 覆盖 {len(meta['categories'])} 个分类, {cmd_count} 命令"

    with open(META_PATH, "w", encoding="utf-8") as f:
        yaml.dump(meta, f)
    print(f"\nTotal added: {total_added}, total commands: {cmd_count}, categories: {len(meta['categories'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
