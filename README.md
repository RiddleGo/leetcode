# labuladong 的算法小抄

> **说明：** 本仓库教程正文中的示例代码已全部转换为 **Python** 版本（原书为 Java/C++ 为主）。算法思路与章节结构保持不变。

## 在线访问

- **学习总入口（推荐）**：https://riddlego.github.io/leetcode/
- **面经导航**：https://riddlego.github.io/interview-hub/index.html

<p align='center'>
<a href="https://labuladong.gitbook.io/algo" target="_blank"><img alt="Website" src="https://img.shields.io/website?label=%E5%9C%A8%E7%BA%BF%E7%94%B5%E5%AD%90%E4%B9%A6&style=flat-square&down_color=blue&down_message=%E7%82%B9%E8%BF%99%E9%87%8C&up_color=blue&up_message=%E7%82%B9%E8%BF%99%E9%87%8C&url=https%3A%2F%2Flabuladong.gitbook.io%2Falgo&logo=Gitea"></a>
<a href="https://github.com/labuladong/fucking-algorithm" target="_blank"><img alt="GitHub" src="https://img.shields.io/github/stars/labuladong/fucking-algorithm?label=Stars&style=flat-square&logo=GitHub"></a>
</p>

<p align='center'>
<a href="https://www.github.com/labuladong" target="_blank"><img src="https://img.shields.io/badge/作者-@labuladong-000000.svg?style=flat-square&logo=GitHub"></a>
<a href="https://www.zhihu.com/people/labuladong" target="_blank"><img src="https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-@labuladong-000000.svg?style=flat-square&logo=Zhihu"></a>
<a href="https://i.loli.net/2020/10/10/MhRTyUKfXZOlQYN.jpg" target="_blank"><img src="https://img.shields.io/badge/公众号-@labuladong-000000.svg?style=flat-square&logo=WeChat"></a>
<a href="https://space.bilibili.com/14089380" target="_blank"><img src="https://img.shields.io/badge/B站-@labuladong-000000.svg?style=flat-square&logo=Bilibili"></a>
</p>
好消息，《labuladong 的算法小抄》出版啦！扫码查看详情，12 月 6 日晚上 12:00 之前限时五折，附赠力扣会员优惠券，扫码即可查看详情👇

![图书二维码](https://i.loli.net/2020/12/03/xXKBpqGzI6ol985.jpg)

<p align='center'>
<img src="https://gitee.com/labuladong/pictures/raw/master/starHistory.png" width = "600" />
</p>


本仓库总共 60 多篇原创文章，都是基于 LeetCode 的题目，涵盖了所有题型和技巧，而且一定要做到**举一反三，通俗易懂**，绝不是简单的代码堆砌，后面有目录。

我先吐槽几句。**刷题刷题，刷的是题，培养的是思维，本仓库的目的就是传递这种算法思维**。我要是只写一个包含 LeetCode 题目代码的仓库，有个锤子用？没有思路解释，没有思维框架，顶多写个时间复杂度，那玩意一眼就能看出来。

只想要答案的话很容易，题目评论区五花八门的答案，动不动就秀 python 一行代码解决，有那么多人点赞。问题是，你去做算法题，是去学习编程语言的奇技淫巧的，还是学习算法思维的呢？你的快乐，到底源自复制别人的一行代码通过测试，已完成题目 +1，还是源自自己通过逻辑推理和算法框架不看答案写出解法？

网上总有大佬喷我，说我写这玩意太基础了，根本没必要啰嗦。我只能说大家刷算法就是找工作吃饭的，不是打竞赛的，我也是一路摸爬滚打过来的，我们要的是清楚明白有所得，不是故弄玄虚无所指。不想办法做到通俗易懂，难道要上来先把《算法导论》吹上天，然后把人家都心怀敬仰地劝退？

**做啥事情做多了，都能发现套路的，我把各种算法套路框架总结出来，相信可以帮助其他人少走弯路**。我这个纯靠自学的小童鞋，花了一年时间刷题和总结，自己写了一份算法小抄，后面有目录，这里就不废话了。

### 使用方法

1、**先给本仓库点个 star，满足一下我的虚荣心**，文章质量绝对值你一个 star。我还在继续创作，给我一点继续写文的动力，感谢。

2、**建议收藏我的 Gitbook 网站，每篇文章开头都有对应的力扣题目链接，可以边看文章边刷题**：

Gitbook 地址：https://labuladong.gitbook.io/algo/

3、建议关注我的公众号 **labuladong**，坚持高质量原创，说是最良心最硬核的技术公众号都不为过。本仓库的文章就是从公众号里整理出来的**一部分**内容，公众号后台回复关键词【电子书】可以获得这份小抄的完整版本；回复【加群】可以加入我们的刷题群，和大家一起讨论算法问题，分享内推机会：

<p align='center'>
<img src="https://gitee.com/labuladong/pictures/raw/master/qrcode.jpg" width = "200" />
</p>

4、欢迎关注 [我的知乎](https://www.zhihu.com/people/labuladong)。

我一直在写优质文章，但是后续的文章只发布到公众号/gitbook/知乎，不能开放到 GitHub。因为本仓库太火了，很多人直接拿我的文章去开付费专栏，价格还不便宜，我这免费写给您看，何必掏冤枉钱呢？所以多多关注本作者，多多宣传，谁也不希望劣币驱逐良币不是么？

其他的先不多说了，直接上干货吧，我们一起搞定 LeetCode，感受一下支配算法的乐趣。

# 目录

* 第1章 核心套路篇
  * [学习算法和刷题的思路指南](reader.html?path=第1章-核心套路篇/1.1-学习算法和刷题的框架思维.md)
  * [动态规划详解](reader.html?path=第1章-核心套路篇/1.2-动态规划解题套路框架.md)
  * [回溯算法详解](reader.html?path=第1章-核心套路篇/1.3-回溯算法解题套路框架.md)
  * [BFS 算法解题套路框架](reader.html?path=第1章-核心套路篇/1.4-BFS 算法套路框架.md)
  * [双指针技巧总结](reader.html?path=第1章-核心套路篇/1.5-双指针技巧套路框架.md)
  * [二分查找详解](reader.html?path=第1章-核心套路篇/1.6-我写了首诗，保你闭着眼睛都能写出二分搜索算法.md)
  * [滑动窗口算法框架](reader.html?path=第1章-核心套路篇/1.7-我写了一个模板，把滑动窗口算法变成了默写题.md)

* 第2章 动态规划系列
  * [动态规划设计：最长递增子序列](reader.html?path=第2章-动态规划系列/2.1-动态规划设计：最长递增子序列.md)
  * [动态规划之正则表达](reader.html?path=第2章-动态规划系列/2.10-动态规划之正则表达式.md)
  * [动态规划：不同的定义产生不同的解法](reader.html?path=第2章-动态规划系列/2.11-不同的定义产生不同的解法.md)
  * [经典动态规划问题：高楼扔鸡蛋](reader.html?path=第2章-动态规划系列/2.12-经典动态规划：高楼扔鸡蛋 .md)
  * [经典动态规划问题：高楼扔鸡蛋（进阶）](reader.html?path=第2章-动态规划系列/2.13-经典动态规划：高楼扔鸡蛋（进阶）.md)
  * [经典动态规划：戳气球](reader.html?path=第2章-动态规划系列/2.14-经典动态规划：戳气球问题.md)
  * [经典动态规划：0-1 背包问题](reader.html?path=第2章-动态规划系列/2.15-经典动态规划：0-1背包问题.md)
  * [经典动态规划：子集背包问题](reader.html?path=第2章-动态规划系列/2.16-经典动态规划：子集背包问题.md)
  * [经典动态规划：完全背包问题](reader.html?path=第2章-动态规划系列/2.17-经典动态规划：完全背包问题.md)
  * 2.18 题目千百变，套路不会变（原文缺失，上游仓库未收录）
  * [动态规划和回溯算法到底谁是谁爹？](reader.html?path=第2章-动态规划系列/2.19-动态规划和回溯算法，到底是什么关系.md)
  * [信封嵌套问题](reader.html?path=第2章-动态规划系列/2.2-二维递增子序列：信封嵌套问题.md)
  * [动态规划设计：最大子数组](reader.html?path=第2章-动态规划系列/2.3-最大子数组问题.md)
  * [动态规划答疑篇](reader.html?path=第2章-动态规划系列/2.4-动态规划答疑：最优子结构及dp 遍历方向.md)
  * [最长公共子序列](reader.html?path=第2章-动态规划系列/2.5-经典动态规划：最长公共子序列.md)
  * [编辑距离](reader.html?path=第2章-动态规划系列/2.6-经典动态规划：编辑距离.md)
  * [动态规划之子序列问题解题模板](reader.html?path=第2章-动态规划系列/2.7-子序列问题解题模板：最长回文子序列.md)
  * [状态压缩：对动态规划进行降维打击](reader.html?path=第2章-动态规划系列/2.8-状态压缩：对动态规划进行降维打击.md)
  * [构造回文的最小插入次数](reader.html?path=第2章-动态规划系列/2.9-以最小插入次数构造回文串.md)

* 第3章 数据结构系列
  * [层层拆解，带你手写 LRU 算法](reader.html?path=第3章-数据结构系列/3.1-手把手教你写LRU缓存淘汰算法.md)
  * [递归反转链表的一部分](reader.html?path=第3章-数据结构系列/3.10-秀操作之纯递归反转链表.md)
  * [如何k个一组反转链表](reader.html?path=第3章-数据结构系列/3.11-秀操作之k个一组反转链表.md)
  * [算法就像搭乐高：带你手撸 LFU 算法](reader.html?path=第3章-数据结构系列/3.2-层层拆解，带你手写LFU算法.md)
  * [二叉搜索树操作集锦](reader.html?path=第3章-数据结构系列/3.3-二叉搜索树操作集锦.md)
  * [如何计算完全二叉树的节点数](reader.html?path=第3章-数据结构系列/3.4-完全二叉树的节点数为什么那么难算.md)
  * [二叉树的序列化，就那几个框架，枯燥至极](reader.html?path=第3章-数据结构系列/3.5-用各种遍历框架序列化和反序列化二叉.md)
  * [Git原理之最近公共祖先](reader.html?path=第3章-数据结构系列/3.6-Git原理之二叉树最近公共祖先.md)
  * [如何使用单调栈解题](reader.html?path=第3章-数据结构系列/3.7-特殊数据结构：单调栈.md)
  * [特殊数据结构：单调队列](reader.html?path=第3章-数据结构系列/3.8-特殊数据结构：单调队列.md)
  * [如何高效判断回文链表](reader.html?path=第3章-数据结构系列/3.9-如何判断回文链表.md)

* 第4章 算法思维系列
  * [回溯算法团灭子集、排列、组合问题](reader.html?path=第4章-算法思维系列/4.1-回溯算法解决子集、组合、排列问题.md)
  * [扁平化嵌套列表](reader.html?path=第4章-算法思维系列/4.10-扁平化嵌套列表.md)
  * [回溯算法最佳实践：解数独](reader.html?path=第4章-算法思维系列/4.2-回溯算法最佳实践：解数独.md)
  * [回溯算法最佳实践：括号生成](reader.html?path=第4章-算法思维系列/4.3-回溯算法最佳实践：括号生成.md)
  * [如何用 BFS 算法秒杀各种智力题](reader.html?path=第4章-算法思维系列/4.4-BFS算法暴力破解各种智力题.md)
  * [twoSum问题的核心思想](reader.html?path=第4章-算法思维系列/4.5-2Sum问题的核心思想.md)
  * [一个函数秒杀 2Sum 3Sum 4Sum 问题](reader.html?path=第4章-算法思维系列/4.6-一个函数解决nSum问题.md)
  * [拆解复杂问题：实现计算器](reader.html?path=第4章-算法思维系列/4.7-拆解复杂问题：实现计算器.md)
  * [烧饼排序算法](reader.html?path=第4章-算法思维系列/4.8-摊烧饼也得有点递归思维.md)
  * [前缀和技巧](reader.html?path=第4章-算法思维系列/4.9-前缀和技巧解决子数组问题.md)

* 第5章 高频面试系列
  * [如何高效寻找素数](reader.html?path=第5章-高频面试系列/5.1-如何高效寻找素数.md)
  * [如何调度考生的座位](reader.html?path=第5章-高频面试系列/5.10-如何调度考生的座位.md)
  * [Union-Find算法详解](reader.html?path=第5章-高频面试系列/5.11-Union-Find算法详解.md)
  * [如何高效进行模幂运算](reader.html?path=第5章-高频面试系列/5.2-如何高效进行模幂运算.md)
  * [如何运用二分查找算法](reader.html?path=第5章-高频面试系列/5.3-如何运用二分查找算法.md)
  * [接雨水问题详解](reader.html?path=第5章-高频面试系列/5.4-如何高效解决接雨水问题.md)
  * [如何去除有序数组的重复元素](reader.html?path=第5章-高频面试系列/5.5-如何去除有序数组的重复元素.md)
  * [如何寻找最长回文子串](reader.html?path=第5章-高频面试系列/5.6-如何寻找最长回文子串.md)
  * [如何运用贪心思想玩跳跃游戏](reader.html?path=第5章-高频面试系列/5.7-如何运用贪心思想玩跳跃游戏.md)
  * [运用贪心算法来做时间管理](reader.html?path=第5章-高频面试系列/5.8-如何运用贪心算法做时间管理.md)
  * [如何判定括号合法性](reader.html?path=第5章-高频面试系列/5.9-如何判定括号合法性.md)
