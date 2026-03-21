# 77. 组合问题：决策树全景解析

为了彻底理解 **“startIndex 顺序去重”** 和 **“搜索范围剪枝 (Range Pruning)”**，我们以 `n=4, k=2` 为例进行深度拆解。

---

## 阶段 1：起始态与第一层决策

起始 `start_index = 1`，我们面临 `1, 2, 3, 4` 四个选择。

```mermaid
graph TD
    Root["(Size: 0) {Path: []}"]
    Root --- |选 1| Node1["(Size: 1) {Path: [1]}" ]
    Root --- |选 2| Node2["(Size: 1) {Path: [2]}"]
    Root --- |选 3| Node3["(Size: 1) {Path: [3]}"]
    Root -.- |"[剪枝] 此时选 4 无意义"| Prune1["不够凑齐 2 个了"]
    
    style Root fill:#f9f,stroke:#333
    style Prune1 fill:#eee,stroke-dasharray: 5 5
```
**逻辑解析**：
- **startIndex**：如果我们选了 `1`，后续只能从 `[2, 3, 4]` 选；选了 `2`，只能从 `[3, 4]` 选。
- **搜索范围剪枝**：当 `k=2` 时，如果我们站在第一层选 `4`，后面由于已经没有数可以选了，导致无法凑齐 2 个，所以 `4` 这个分支直接被剪掉。

---

## 阶段 2：纵向深入 (以 [1] 为例)

来到第二层，我们在 `[1]` 的基础上继续搜选，`start_index = 2`。

```mermaid
graph TD
    Node1["(Size: 1) {Path: [1]}"]
    Node1 --- |选 2| Node1_1["(Size: 2) {Path: [1, 2]} ✅"]
    Node1 --- |选 3| Node1_2["(Size: 2) {Path: [1, 3]} ✅"]
    Node1 --- |选 4| Node1_3["(Size: 2) {Path: [1, 4]} ✅"]
    
    style Node1 fill:#bbf,stroke:#333
    style Node1_1 fill:#8f8,stroke:#333
    style Node1_2 fill:#8f8,stroke:#333
    style Node1_3 fill:#8f8,stroke:#333
```
**逻辑解析**：
- 此时 `len(path) == k`，满足终止条件，记录答案并回溯。

---

## 阶段 3：剪枝案例说明 (n=4, k=3)

假设我们要选 3 个数，看看剪枝如何工作：

```mermaid
graph TD
    R["(0) []"]
    R --- |选 1| N1["(1) [1]"]
    R --- |选 2| N2["(2) [2]"]
    R -.- |"[剪枝] 必死无疑"| P["3 和 4 都不用看了"]
    
    style R fill:#f9f,stroke:#333
    style P fill:#f88,stroke:#333
```
**逻辑解析**：
- 如果要在 `[1, 2, 3, 4]` 选 3 个，选 `3` 会由于后面只剩一个 `4` 而无法凑齐。
- 所以第一层我们只需要尝试 `1` 和 `2` 即可。

---

## 总结：剪枝公式的第一性原理

> **`range(start_index, n - (k - len(path)) + 2)`**

- `k - len(path)`：代表我们**还需要**几个数。
- `n - (...) + 1`：代表为了凑齐剩下的数，我们**最晚**必须从哪开始选。
- 这个公式将“无效路径”在进入递归前直接砍掉，避免了海量的函数调用开销。

---
*你可以直接在 IDE 中打开此文件预览效果。*
