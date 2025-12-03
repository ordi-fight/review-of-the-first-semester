# 🐍 Python 抽象基類 (ABC) 與繼承指南

這份文件總結了 Python 中使用 `abc` 模組建立抽象基類（Abstract Base Class）的關鍵原則，以及如何正確處理方法繼承、實作抽象方法，與 `NotImplementedError` 的使用時機。

## 1. 抽象基類 (ABC) 的核心概念

抽象基類（ABC）用於定義一個**介面**或**契約**。它強制所有繼承的非抽象子類都必須實作基類中定義的抽象方法。

| 特性 | 說明 | 程式碼關鍵字 |
| :--- | :--- | :--- |
| **定義類** | 類別必須繼承自 `ABC`。 | `from abc import ABC` |
| **抽象方法** | 該方法在基類中沒有具體邏輯，**必須**由子類實作。 | `@abstractmethod` |
| **實作要求** | 如果子類沒有實作所有抽象方法，Python 在嘗試實例化時會拋出 `TypeError`。 | N/A (Python 自動檢查) |

## 2. 方法分類與繼承處理原則

基類中方法的定義方式，決定了子類對它的處理方式：**繼承使用**或**強制實作**。

### A. 通用非抽象方法 (允許繼承)

這類方法在基類中提供了完整的、所有子類通用的邏輯。子類可以選擇不實作（不覆寫），直接繼承使用。

**原則：** 在基類中完成邏輯實作，**絕不**在方法結尾使用 `raise NotImplementedError`。

| 方法 | 目的與處理方式 | 程式碼範例 (`BasePlaylist`) |
| :--- | :--- | :--- |
| `__init__` | 完成屬性初始化。 | 移除 `raise NotImplementedError`。 |
| `add()` | 完成曲目新增邏輯。 | 移除 `raise NotImplementedError`。 |
| `__len__` | 返回曲目數量。 | 移除 `raise NotImplementedError`，讓方法執行 `return len(self._tracks)`。 |
| `__repr__` | 返回可讀的物件表示。 | 移除 `raise NotImplementedError`。 |

**錯誤範例說明：** 如果您在 `__len__` 結尾加上 `raise NotImplementedError`，程式將永遠無法執行到 `return len(self._tracks)`，導致邏輯失效。

### B. 抽象方法 (強制實作)

這類方法是基類定義的契約，必須由子類提供具體的實現邏輯。

**原則：** 子類**必須**覆寫此方法。基類中的方法體通常為 `pass`。

| 方法 | 目的與處理方式 | 程式碼範例 (`SequentialPlaylist`) |
| :--- | :--- | :--- |
| `__iter__` | 定義播放清單的迭代邏輯。 | **必須實作**：定義一個生成器 (`yield`) 或返回一個迭代器 (`return iter(self._tracks)`)。 |

## 3. `raise NotImplementedError` 的正確用途

`raise NotImplementedError` 的核心作用是標記某個方法在**當前類別**中是**未實作**的，它主要用於以下情況：

| 使用情境 | 說明 | 程式碼 / 行為 |
| :--- | :--- | :--- |
| **手動強制覆寫** | 當您未使用 `abc` 模組，但希望強制子類覆寫某個方法時，可以在基類中手動拋出此錯誤。 | ```python def play(self): raise NotImplementedError("Subclasses must implement play()") ``` |
| **不支持的運算** | 當實作特殊方法如 `__add__` 或 `__eq__` 時，遇到不兼容的類型，用來指示操作不被支持。 | `return NotImplemented`（比拋出錯誤更優）或 `raise NotImplementedError`。 |

**錯誤排除：**

如果您在運行時遇到 `NotImplementedError`，最可能的原因是：
1. **您手動在已經完成實作的方法（如 `__len__`）結尾，錯誤地保留了 `raise NotImplementedError` 語句。** (這是您程式碼中需要修正的主要問題)
2. 您呼叫了一個被設計為必須在子類中覆寫的方法（如上述手動強制覆寫的 `play()`）。
# 🔢 Python 運算符重載 (Operator Overloading) 精髓指南

運算符重載是 Python 面向對象編程中的一個強大特性，它允許我們為自定義類別定義標準運算符（如 `+`, `-`, `==` 等）的行為，使其能像內建類型一樣直觀地使用。

---

## 1. 運算符重載的原理：魔術方法 (Magic Methods)

在 Python 中，所有標準的運算符操作都是通過呼叫物件內建的特殊方法（稱為**魔術方法**，Magic Methods，以雙底線 `__` 開頭和結尾）來實現的。

當您對物件使用運算符時，Python 會在內部執行對應的方法呼叫：

| 運算符 | 內建類型範例 | 對應的魔術方法 | 語義 (Semantic) |
| :---: | :--- | :--- | :--- |
| `+` | `1 + 2` | `__add__(self, other)` | 加法或合併操作 |
| `-` | `5 - 3` | `__sub__(self, other)` | 減法操作 |
| `*` | `3 * 4` | `__mul__(self, other)` | 乘法或重複操作 |
| `==` | `A == B` | `__eq__(self, other)` | 相等性比較 |
| `<` | `A < B` | `__lt__(self, other)` | 小於比較 (Less Than) |

---

## 2. 運作機制：`self` 與 `other` 的角色

對於二元運算（如 $A + B$），Python 會遵循一套嚴格的查找和呼叫流程來決定 `self` 和 `other`。

### 核心機制：左邊物件優先

當執行 $A + B$ 時，Python 的處理順序是：

1. **優先查找 $A$ (左側運算元)：** 嘗試呼叫 $A$ 的 `__add__` 方法，並將 $B$ 作為參數傳入。

    class1 (object) + class2(object)
   
    "+" call class1 method __add__(self,other)
   
    class2 is viewed as argument other

3. **如果 $A$ 不支持：** 如果 $A$ 沒有定義 `__add__`，或者 `A.__add__(B)` 返回了 `NotImplemented`，Python 會嘗試呼叫 $B$ 的**反射**方法 `__radd__`，並將 $A$ 作為參數傳入。

### 角色分配

* **`self`：** 永遠是**運算符左側**的物件實例（發起呼叫者）。
* **`other`：** 永遠是**運算符右側**的物件實例（作為參數傳入）。

### 範例：播放列表相加 (`playlists[l1] + playlists[l2]`)

| 程式碼 | 內部呼叫 | `self` | `other` |
| :--- | :--- | :--- | :--- |
| `A + B` | `A.__add__(B)` | `A` 實例 | `B` 實例 |
| `playlists[l1] + playlists[l2]` | `playlists[l1].__add__(playlists[l2])` | `playlists[l1]` (左側) | `playlists[l2]` (右側) |

---

## 3. 關鍵精髓與注意事項

### 萬物皆物件 (Everything is an Object)

這套機制適用於 Python 中的所有元素，包括內建類型：

* **整數相加：** `1 + 2` 實質上等同於 `(1).__add__(2)`。其中 `1` 是 `int` 類別的實例，其 `__add__` 方法被呼叫。
* **列表合併：** `[1] + [2]` 實質上等同於 `[1].__add__([2])`，觸發了 `list` 內建的合併操作。

### 返回新物件 (Immutability Principle)

對於像 `__add__` 這樣的二元運算，最佳實踐是**創建並返回一個新的物件**，而不是修改 `self` 實例（除非您實作的是原地運算，如 `__iadd__` 對應的 `+=`）。

在您的 `Playlist` 範例中，這是正確的：

```python
def __add__(self, other):
    # 創建一個新的 SequentialPlaylist 實例
    new_player = SequentialPlaylist() 
    
    # 使用列表的 + 運算符合併曲目 (創建新列表)
    new_player.track = self.track + other.track 
    
    # 返回新物件
    return new_player
