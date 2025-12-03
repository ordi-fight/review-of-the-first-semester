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
