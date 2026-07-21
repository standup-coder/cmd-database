package data

import (
	"sync"
	"testing"
)

func TestCacheGetSet(t *testing.T) {
	cache := NewCache(3)

	val, ok := cache.Get("key1")
	if ok {
		t.Error("expected miss for empty cache")
	}
	if val != nil {
		t.Errorf("expected nil value, got %v", val)
	}

	cache.Set("key1", "value1")
	val, ok = cache.Get("key1")
	if !ok {
		t.Error("expected hit for key1")
	}
	if val != "value1" {
		t.Errorf("expected 'value1', got %v", val)
	}
}

func TestCacheLRUEviction(t *testing.T) {
	cache := NewCache(3)

	cache.Set("a", 1)
	cache.Set("b", 2)
	cache.Set("c", 3)

	_, ok := cache.Get("a")
	if !ok {
		t.Error("expected 'a' to still be in cache")
	}

	cache.Set("d", 4)

	_, ok = cache.Get("b")
	if ok {
		t.Error("expected 'b' to be evicted (LRU)")
	}

	val, ok := cache.Get("a")
	if !ok || val != 1 {
		t.Error("expected 'a' to still be in cache (recently accessed)")
	}

	val, ok = cache.Get("d")
	if !ok || val != 4 {
		t.Error("expected 'd' to be in cache")
	}
}

func TestCacheUpdate(t *testing.T) {
	cache := NewCache(5)

	cache.Set("key", "old")
	cache.Set("key", "new")

	val, ok := cache.Get("key")
	if !ok {
		t.Error("expected hit")
	}
	if val != "new" {
		t.Errorf("expected 'new', got %v", val)
	}
}

func TestCacheClear(t *testing.T) {
	cache := NewCache(5)
	cache.Set("a", 1)
	cache.Set("b", 2)

	cache.Clear()

	if cache.Size() != 0 {
		t.Errorf("expected size 0 after clear, got %d", cache.Size())
	}

	_, ok := cache.Get("a")
	if ok {
		t.Error("expected miss after clear")
	}
}

func TestCacheSize(t *testing.T) {
	cache := NewCache(10)
	if cache.Size() != 0 {
		t.Errorf("expected size 0, got %d", cache.Size())
	}

	cache.Set("a", 1)
	cache.Set("b", 2)
	if cache.Size() != 2 {
		t.Errorf("expected size 2, got %d", cache.Size())
	}
}

func TestCacheConcurrentAccess(t *testing.T) {
	cache := NewCache(100)
	var wg sync.WaitGroup

	for i := 0; i < 1000; i++ {
		wg.Add(1)
		go func(n int) {
			defer wg.Done()
			key := string(rune('a' + n%26))
			cache.Set(key, n)
			cache.Get(key)
		}(i)
	}

	wg.Wait()
}

func TestCacheMaxSizeOne(t *testing.T) {
	cache := NewCache(1)

	cache.Set("a", 1)
	cache.Set("b", 2)

	_, ok := cache.Get("a")
	if ok {
		t.Error("expected 'a' to be evicted when maxSize=1")
	}

	val, ok := cache.Get("b")
	if !ok || val != 2 {
		t.Error("expected 'b' to be in cache")
	}
}

func TestSearchCacheTypeAssertionSafety(t *testing.T) {
	sc := NewSearchCache(10)

	sc.cache.Set("bad_key", "not a command slice")
	_, ok := sc.GetSearchResult("bad_key")
	if ok {
		t.Error("expected false when non-[]*model.Command value is stored")
	}

	sc.cache.Set("bad_key2", 42)
	_, ok = sc.GetSearchResult("bad_key2")
	if ok {
		t.Error("expected false when integer value is stored")
	}

	sc.cache.Set("bad_key3", []string{"not", "commands"})
	_, ok = sc.GetSearchResult("bad_key3")
	if ok {
		t.Error("expected false when []string value is stored")
	}

	sc.cache.Set("bad_key4", nil)
	_, ok = sc.GetSearchResult("bad_key4")
	if ok {
		t.Error("expected false when nil value is stored")
	}

	_, ok = sc.GetSearchResult("nonexistent")
	if ok {
		t.Error("expected false for nonexistent key")
	}
}

func TestCacheConcurrentAccessHeavy(t *testing.T) {
	cache := NewCache(50)
	var wg sync.WaitGroup

	for i := 0; i < 5000; i++ {
		wg.Add(1)
		go func(n int) {
			defer wg.Done()
			key := string(rune('a'+n%26)) + string(rune('0'+n%10))
			cache.Set(key, n)
			cache.Get(key)
			cache.Size()
			if n%100 == 0 {
				cache.Clear()
			}
		}(i)
	}

	wg.Wait()
}

func TestSearchCacheConcurrentSetGet(t *testing.T) {
	sc := NewSearchCache(100)
	var wg sync.WaitGroup

	for i := 0; i < 2000; i++ {
		wg.Add(1)
		go func(n int) {
			defer wg.Done()
			key := string(rune('a' + n%26))
			sc.SetSearchResult(key, nil)
			sc.GetSearchResult(key)
			if n%50 == 0 {
				sc.Clear()
			}
		}(i)
	}

	wg.Wait()
}
