---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
lang: zh
---

> 从 40 条内容中筛选出 28 条重要资讯。

---

1. [Anthropic 公开发布 Claude 模型系统提示词](#item-1) ⭐️ 8.0/10
2. [模型故意变笨：从记忆转向工具调用](#item-2) ⭐️ 8.0/10
3. [Stripe 敲定收购 AI 模型市场 OpenRouter，交易额超 70 亿美元](#item-3) ⭐️ 8.0/10
4. [Claude AI 自主维护 App：388 个 PR 中 180 个被合并](#item-4) ⭐️ 8.0/10
5. [Reddit 帖子质疑 ECA 论文核心假设](#item-5) ⭐️ 8.0/10
6. [嵌入式工程师回应 RISC-V 批评：成本与开放性为发展中国家带来优势](#item-6) ⭐️ 7.0/10
7. [AI 积分转售经济](#item-7) ⭐️ 7.0/10
8. [OpenAI 设计负责人称当下是设计师的最佳时代](#item-8) ⭐️ 7.0/10
9. [Inception Point 打造用于播客、时尚、影视和音乐的 AI 虚拟人物](#item-9) ⭐️ 7.0/10
10. [Claude AI 在 54 小时黎曼猜想尝试中取得数学突破](#item-10) ⭐️ 7.0/10
11. [法国总理将就税务机构网络攻击召开危机会议](#item-11) ⭐️ 7.0/10
12. [菲尔兹奖得主高尔斯：LLM 解数学难题多靠反例而非证明](#item-12) ⭐️ 7.0/10
13. [Hugging Face 称 Qwen 衍生模型超 15.1 万，成开放模型生态重要基础](#item-13) ⭐️ 7.0/10
14. [Qwen3.8-27B 表现出色，但默认设置导致过度思考](#item-14) ⭐️ 7.0/10
15. [SSOG-Attention：可分离高斯和实现次二次注意力](#item-15) ⭐️ 7.0/10
16. [线性注意力在 DNA 大海捞针回忆测试中失败](#item-16) ⭐️ 7.0/10
17. [Firefox iOS 版新增内置广告拦截功能](#item-17) ⭐️ 6.0/10
18. [AI 创造的新问题及人们的应对之道](#item-18) ⭐️ 6.0/10
19. [Face2Gene 等 AI 工具在罕见病诊断中应用增多](#item-19) ⭐️ 6.0/10
20. [AI 与数据中心政策成美国中期选举重要议题，约四成选战提及](#item-20) ⭐️ 6.0/10
21. [索尼 CEO 十时裕树推动公司向娱乐业务转型](#item-21) ⭐️ 6.0/10
22. [Pathway 获 3000 万美元种子轮，估值 5 亿美元，主攻后 Transformer 架构](#item-22) ⭐️ 6.0/10
23. [中国民众对 AI 比美国更乐观，视其为低破坏工具](#item-23) ⭐️ 6.0/10
24. [SineKAN：使用正弦激活函数的柯尔莫哥洛夫-阿诺德网络](#item-24) ⭐️ 6.0/10
25. [Riley Brown 使用 OpenAI Codex 运营百万粉丝内容业务](#item-25) ⭐️ 5.0/10
26. [马来西亚第二季度 GDP 增长 6%，受芯片制造和数据中心建设推动](#item-26) ⭐️ 5.0/10
27. [BlackBerry 实现 2017 年来首次 Q1 现金正增长，得益于 QNX 和 Secusmart](#item-27) ⭐️ 5.0/10
28. [应届生寻求物理 AI 与机器人职业指导](#item-28) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Anthropic 公开发布 Claude 模型系统提示词](https://platform.claude.com/docs/en/release-notes/system-prompts) ⭐️ 8.0/10

Anthropic 已在平台文档网站上公开发布 Claude 模型的官方系统提示词，让公众可以直接查看这些模型接收的隐藏指令。Hacker News 讨论中，Simon Willison 提供了一个将系统提示词重建为 git 提交历史的工具，并重点展示了 Opus 4.8 与 Opus 5 之间的差异。 此举提高了对 AI/LLM 从业者的透明度，使他们能够更好地理解模型行为、调试提示词交互并优化应用设计。它还可能促使其他厂商公开类似细节，并加强正在兴起的上下文工程实践。 评论者指出这些公开的提示词非常长，而 Opus 5 中一个引人注目的新增内容是：Claude 被要求在回应“存在图片”的说法前自行确认图片是否真的存在。Simon Willison 的仓库将每个版本的系统提示词转换成一个 git 提交，便于审查版本之间的提示词变化。

hackernews · tosh · 8月16日 12:48 · [社区讨论](https://news.ycombinator.com/item?id=49319556)

**背景**: 系统提示词是在任何用户消息到达之前就告诉大语言模型如何行为的初始指令集，厂商通常会对这些指令保密。提示工程是指设计和优化这些指令以获得更有用、更准确输出的实践。公开发布系统提示词仍相对少见，部分原因是它们可能暴露内部设计选择，并可能成为提示注入攻击的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/System_prompt">System prompt</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_engineering">Prompt engineering</a></li>

</ul>
</details>

**社区讨论**: 讨论普遍对这种透明度持正面态度，Simon Willison 分享的基于 git 的差异比较工具也受到不少人认可。一些评论者认为这些提示词过于冗长，另一些人则指出部分指令只是在陈述常识，令人质疑模型对其依赖程度。此外，还有一条离题讨论质疑 Hacker News 是否在压制对 AI 持负面态度的报道。

**标签**: `#AI`, `#Claude`, `#System Prompts`, `#Prompt Engineering`, `#LLM`

---

<a id="item-2"></a>
## [模型故意变笨：从记忆转向工具调用](https://w4g1.dev/blog/models-are-getting-dumber-on-purpose) ⭐️ 8.0/10

一篇引发广泛讨论的分析文章认为，AI 模型正在被有意“变笨”，即在事实记忆方面变弱，转而调用检索、搜索和计算器等外部工具，以降低幻觉和知识过时。 这一转变可能降低重新训练成本，使回答更可验证，并支持特定领域部署，但也改变了模型能力的评估方式，并引发对内部知识与推理未来角色的思考。 文章引用了不允许使用工具的 SimpleQA 事实回忆基准，Gemini 2.5 Pro 得分 53%，并对比了 RAG（2020 年）和 Meta 的 Toolformer（2023 年）等方法；评论者指出 SimpleQA 可能已过时，并提到一个名为 Needle 的 14MB 工具调用模型。

hackernews · hruvhwe · 8月16日 19:04 · [社区讨论](https://news.ycombinator.com/item?id=49322695)

**背景**: 检索增强生成（RAG）于 2020 年提出，让大语言模型在回答前从外部来源检索信息，从而提高准确性并减少幻觉。Toolformer（2023 年）展示了模型可以自主学习何时以及如何调用计算器、搜索引擎等 API。传统大语言模型将知识存储在训练得到的权重中，而工具导向的模型则把事实交给外部系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>
<li><a href="https://arxiv.org/abs/2302.04761">[2302.04761] Toolformer: Language Models Can Teach Themselves ...</a></li>

</ul>
</details>

**社区讨论**: 评论观点不一：有人提出可插拔知识库，将通用推理与专业知识结合；也有人认为把知识与推理解耦是一种幻想，因为推理依赖世界知识。还有评论者指出该文章似乎是 AI 生成的，且其用 Gemini 2.5 Pro 进行的 SimpleQA 对比已经过时。

**标签**: `#AI`, `#LLMs`, `#Machine Learning`, `#Knowledge Retrieval`, `#Model Design`

---

<a id="item-3"></a>
## [Stripe 敲定收购 AI 模型市场 OpenRouter，交易额超 70 亿美元](https://www.techmeme.com/260816/p9#a260816p9) ⭐️ 8.0/10

据彭博社消息，Stripe 已敲定以超过 70 亿美元收购 AI 模型市场 OpenRouter 的协议，而今年 5 月 OpenRouter 估值仅为 13 亿美元。 这笔交易表明 AI 模型路由与市场正成为关键基础设施，Stripe 可能将支付与 AI 模型计费深度整合，影响开发者与企业采用 AI 的方式。 OpenRouter 提供统一 API，接入 80 多家提供商的 500 多个模型，服务 25 万多个应用和 420 多万用户；交易估值是 5 月估值（13 亿美元）的 5 倍以上。

rss · Techmeme · 8月16日 20:10

**背景**: OpenRouter 是一个聚合平台，通过统一 API 让开发者访问 OpenAI、Anthropic、Google 等多家提供商的大语言模型，并处理路由、计费和合规。Stripe 是大型支付基础设施公司，收购 OpenRouter 后可能原生提供 AI 模型使用计费与变现能力。随着企业和应用需要灵活调用多个模型，AI 模型市场正在快速增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenRouter">OpenRouter</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**标签**: `#Stripe`, `#OpenRouter`, `#AI`, `#acquisition`, `#model marketplace`

---

<a id="item-4"></a>
## [Claude AI 自主维护 App：388 个 PR 中 180 个被合并](http://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652718121&idx=2&sn=566e5ce1a30840fa891e3a5364bc0537&chksm=f07e9ef612704352f79179021d440f9c92b4d31224960664cd3562145c718f18bdb7cbb97ff9&scene=126&sessionid=0#rd) ⭐️ 8.0/10

Claude 之父 Boris Cherny 进行了一项实验，让 Claude AI 通过 Slack 频道全权负责其 App 的日常维护；AI 自主提交了 388 个 PR，其中 180 个被合并，所有代码均由 AI 编写。 这验证了 AI 自主软件维护的可行性，并预示未来开发范式可能变为开发者主要负责审查和批准 AI 生成的变更，从而显著改变 DevOps 中的角色分工。 实验涵盖 bug 修复、依赖更新和小功能迭代，覆盖 iOS、Android、桌面端、Web、CLI 和 Agent SDK 六类环境；但存在边界模糊、复杂重构受限等局限。

baaihub · 新智元 · 8月16日 07:20

**背景**: Claude 是 Anthropic 开发的大语言模型系列，Claude Code 是其智能体编程工具，可以理解代码库、编辑文件并运行命令。PR（Pull Request）是提交代码变更以供审核、再合并到主代码库的机制。Boris Cherny 的实验将 Claude Code 接入 Slack 频道，让 AI 自动执行应用维护任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>

</ul>
</details>

**标签**: `#AI`, `#DevOps`, `#Software Engineering`, `#Claude`, `#Autonomous Coding`

---

<a id="item-5"></a>
## [Reddit 帖子质疑 ECA 论文核心假设](https://www.reddit.com/r/MachineLearning/comments/1vptaw9/revisiting_the_efficient_channel_attention_paper/) ⭐️ 8.0/10

一条 Reddit 帖子批评了高被引的高效通道注意力（ECA）论文，认为在通道均值上做一维卷积假设了通道维度并不具备的拓扑结构。作者在国际象棋残局库上的实验显示，即使核大小 k=1，ECA 也明显优于压缩-激励（SE），削弱了该论文关于跨通道交互是关键成分的说法。 该批评质疑了一个被引用超过 12000 次的常用注意力模块的根本依据，可能影响研究者对通道注意力机制的理解。它可能推动更具原则性的架构设计，并促使人们重新审视 ECA 的实际工作机制。 ECA 通过对全局平均池化后的通道特征做自适应核大小 k 的快速一维卷积来避免降维。在作者的棋局残局库实验中，ECA k=3 的精度为 96.68%，k=1 为 96.61%，而 SE8 为 96.17%，恒等门控为 96.04%；该帖子还指出卷积依赖局部性和平移不变性，但通道顺序是任意的。

reddit · r/MachineLearning · /u/arkuto · 8月16日 10:13

**背景**: 通道注意力机制用于对卷积神经网络的特征通道进行重新标定；压缩-激励模块先做全局平均池化，再用两个带瓶颈的全连接层生成通道权重。高效通道注意力（ECA）于 2019 年提出、2020 年发表在 CVPR 上，去掉了瓶颈结构，改用一维卷积捕获跨通道交互，参数更少。卷积本身适合具有空间或时间局部性和平移不变性的数据，如图像或序列；而通道索引通常没有内在的拓扑顺序。国际象棋残局库是包含最多六个棋子的已完全求解数据集，可以为架构评测提供无偏采样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1910.03151">[1910.03151] ECA-Net: Efficient Channel Attention for Deep ... ECA-Net: Efficient Channel Attention - GitHub Efficient Channel Attention - emergentmind.com ECA-Net: Efficient Channel Attention for Deep Convolutional ... 即插即用模块 ECA-Net: Efficient Channel Attention for Deep ... Efficient Channel Attention: A Comprehensive Guide for 2025 ... [1910.03151] ECA-Net: Efficient Channel Attention for Deep ...</a></li>
<li><a href="https://github.com/BangguWu/ECANet">ECA-Net: Efficient Channel Attention - GitHub Efficient Channel Attention - emergentmind.com ECA-Net: Efficient Channel Attention for Deep Convolutional ... 即插即用模块 ECA-Net: Efficient Channel Attention for Deep ... Efficient Channel Attention: A Comprehensive Guide for 2025 ... [1910.03151] ECA-Net: Efficient Channel Attention for Deep ...</a></li>
<li><a href="https://www.emergentmind.com/topics/efficient-channel-attention">Efficient Channel Attention - emergentmind.com</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#computer vision`, `#attention mechanism`, `#ECA`, `#convolutional neural networks`

---

<a id="item-6"></a>
## [嵌入式工程师回应 RISC-V 批评：成本与开放性为发展中国家带来优势](https://rvembedded.com/blog_post/12/) ⭐️ 7.0/10

一位来自特立尼达和多巴哥的嵌入式工程师发表了对早前批评文章《RISC-V They Should Have Known Better》的回应，认为 RISC-V 的开放标准和低单位成本对嵌入式开发人员和发展中国家的工程师尤为有利。该帖在 Hacker News 上获得 370 分和 193 条评论，引发热烈讨论。 这一回应将讨论焦点从高端性能争论转移到嵌入式系统的成本和可及性上，而 RISC-V 在该领域已得到大量采用。它凸显了开放指令集架构如何降低发展中地区开发者的门槛，并可能影响未来的硬件选择。 该回应主要关注嵌入式用例，而没有直接回应对碎片化以及相比 ARM64 性能不佳的批评。评论者指出一个可能的矛盾：作者称需支付 60 至 200 美元运费来购买 1 美元芯片，因此所谓 10 美分 RISC-V 芯片可能并未实质降低其所在地区的总成本。

hackernews · Narishma · 8月16日 17:01 · [社区讨论](https://news.ycombinator.com/item?id=49321717)

**背景**: RISC-V 是一种免费开放的指令集架构（ISA），最初由加州大学伯克利分校开发，现由 RISC-V International 维护；与 x86 和 ARM 等专有 ISA 不同，它无需支付版税即可实现。嵌入式系统是嵌入在更大设备中的专用计算机，通常大批量生产且对成本高度敏感，因此廉价且可定制的处理器内核颇具吸引力。RISC-V 的模块化扩展允许定制，但也可能导致软件碎片化，这是常见的批评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC-V">RISC-V</a></li>
<li><a href="https://en.wikipedia.org/wiki/Instruction_set_architecture">Instruction set architecture</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embedded_system">Embedded system</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论意见不一。一些评论者认为作者在回避原文对 RISC-V 碎片化和嵌入式以外性能不足的批评；另一些人则认为 RISC-V 的性能会像 x86 一样随时间提升。还有多人指出运费远高于芯片价格，削弱了作者关于 10 美分部件成本优势的说法。

**标签**: `#RISC-V`, `#embedded systems`, `#hardware`, `#ISA`, `#open source`

---

<a id="item-7"></a>
## [AI 积分转售经济](https://vectoral.com/blog/who-are-the-token-brokers) ⭐️ 7.0/10

文章分析了日益增长的 AI 计算积分灰色市场，描述了代币经纪商和中继服务如何转售来自 OpenAI 等提供商的未使用或欺诈性获得的 API 积分。文章还指出了信任、安全和滥用问题，例如一名 YC 创业学校参与者试图转售 2500 美元积分。 这一市场值得关注，因为它揭示了 API 积分被滥用和转售的容易程度，可能破坏平台服务条款，使未经授权的模型访问成为可能，并给买家带来安全风险；它影响 AI 提供商、合法初创公司以及被低价吸引的用户。 代币经纪商充当访问令牌的中介，中继服务转发 API 调用；滥用模式包括自动创建账户、转售被盗账户和模型蒸馏。买家往往无法验证实际获得的是哪个模型，转售积分也违反平台协议。

hackernews · mlenhard · 8月16日 14:44 · [社区讨论](https://news.ycombinator.com/item?id=49320611)

**背景**: AI 积分是用于访问 AI 模型 API 的预付费或促销单元，通常分发给初创公司或开发者。代币经纪商是发行或刷新访问令牌的中介，中继服务则在客户端与 API 之间转发请求；在这一灰色市场中，这些机制被重新用于官方渠道之外的访问转售。这可能违反服务条款，并带来信任、安全和验证方面的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.revenera.com/blog/software-monetization/ai-credits-step-by-step-guide/">AI Credits : Your Step-by-Step Guide to Monetizing AI</a></li>
<li><a href="https://nhimg.org/glossary/token-broker/">What Is Token Broker ? Definition & Examples</a></li>
<li><a href="https://en.wikipedia.org/wiki/Relay_services">Relay services</a></li>

</ul>
</details>

**社区讨论**: 评论对信任匿名第三方来处理私人数据表示担忧，指出此类滥用模式已有数十年历史，并认为转售者可通过 IP 地址被识别且账户会被标记。还有人认为研究过于浅显，指出 linux.do 或 nodeseek.com 等平台上的代币转售经济更为庞大；有人质疑买家如何验证所购模型。

**标签**: `#AI`, `#security`, `#gray market`, `#API credits`, `#OpenAI`

---

<a id="item-8"></a>
## [OpenAI 设计负责人称当下是设计师的最佳时代](https://www.lennysnewsletter.com/p/openais-head-of-design-this-is-the) ⭐️ 7.0/10

OpenAI 产品设计负责人 Ian Silber 在 Lenny's Newsletter 的访谈中表示，AI 对设计师而言是机遇而非威胁，并讨论了人类设计师仍然优于 AI 的领域以及如何应对快速变化带来的压力。 这次访谈将 AI 重新定义为能够增强设计工作流程的工具，有助于缓解设计师的焦虑，并指导专业人士在生成式 AI 深入产品开发时调整自身技能。 该内容以播客节目形式呈现，侧重于职业与策略层面的见解，而非深度的技术实现，涵盖人类判断力和审美品味仍让设计师占优势的领域。

rss · Lenny's Podcast · 8月16日 12:31

**背景**: OpenAI 是一家领先的人工智能研究机构，以 GPT-4 等模型和 ChatGPT 等产品闻名。Lenny's Newsletter 是一个广受关注、覆盖产品管理、设计与科技的出版物和播客。随着 AI 工具越来越多地自动化设计流程的部分环节，许多设计师担心岗位被取代以及需要学习新技能。

**标签**: `#AI`, `#design`, `#interview`, `#OpenAI`, `#product design`

---

<a id="item-9"></a>
## [Inception Point 打造用于播客、时尚、影视和音乐的 AI 虚拟人物](https://www.techmeme.com/260816/p12#a260816p12) ⭐️ 7.0/10

《纽约时报》2026 年 8 月 13 日报道，Inception Point 等初创公司正在打造 AI 虚拟人物（如 Claire Delish、VV Steele、Nigel Thistledown 和 Lila Walker），这些人物可以主持播客、展示服装，并出现在媒体、时尚、影视和音乐等领域。 这表明生成式 AI 正从工具转向面向受众的品牌化虚拟角色，可能重塑创意产业的内容生产和人才经济，同时也引发对真实性、劳动替代和低质量合成媒体的担忧。 Inception Point 管理着 50 多个 AI 虚拟人物，根据一项行业分析，它每周生成约 3000 集带 iHeart Media 广告的播客；但批评者将其中的许多内容描述为几乎没有听众的 AI 垃圾内容。

rss · Techmeme · 8月17日 00:40

**背景**: AI 虚拟人物是拥有名字、形象、声音和背景故事的数字化角色，用于吸引受众。Inception Point 利用生成式 AI（包括与 Hume AI 等伙伴合作的情感语音模型）来大规模创建这些人物，用于播客、短视频和其他媒体。这延续了虚拟网红和合成媒体在娱乐领域的发展趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.inceptionpoint.ai/">Inception Point AI – InceptionPoint AI — AI-Powered Personality Creators</a></li>
<li><a href="https://www.hume.ai/blog/case-study-hume-inception-point">Creating Podcasts at Scale with Inception Point | Hume Blog | Hume AI</a></li>
<li><a href="https://pivot-to-ai.com/2025/09/10/inception-point-ai-spam-podcasts-with-no-listeners/">Inception Point — AI spam podcasts with no listeners</a></li>

</ul>
</details>

**标签**: `#AI personas`, `#media industry`, `#fashion technology`, `#generative AI`, `#creative industries`

---

<a id="item-10"></a>
## [Claude AI 在 54 小时黎曼猜想尝试中取得数学突破](https://www.techmeme.com/260816/p11#a260816p11) ⭐️ 7.0/10

据《华尔街日报》报道，一个 Claude 模型在尝试解决黎曼猜想的 54 小时过程中取得了数学突破，尽管这次尝试最终未成功。该模型在用户反复鼓励后持续进行。 这表明先进 AI 模型不仅具有超越人类的数学能力，还可能受到类似人类的激励信号影响，这对人机协作和提示策略具有重要意义。同时也凸显了当前 AI 在攻克开放问题时的潜力与局限。 这次尝试持续了 54 小时，未能证明黎曼猜想，但据报道产生了显著的数学突破。报道指出，目前最聪明的 AI 模型在数学上已“超越人类”，但仍会对人类的道义支持和鼓励作出回应。

rss · Techmeme · 8月16日 22:35

**背景**: Claude 是 Anthropic 开发的大型语言模型系列，以注重安全性和有用性著称。黎曼猜想是一个著名的未解猜想，断言黎曼 zeta 函数的所有非平凡零点的实部都为 1/2，它也是克莱数学研究所的千禧年大奖难题之一。尽管有大量数值证据，但目前尚无证明。这则新闻建立在 AI 数学推理近期进展的基础上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Riemann_hypothesis">Riemann hypothesis</a></li>
<li><a href="https://www.claymath.org/millennium/riemann-hypothesis/">Riemann Hypothesis - Clay Mathematics Institute</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#Riemann hypothesis`, `#Anthropic`, `#LLM behavior`

---

<a id="item-11"></a>
## [法国总理将就税务机构网络攻击召开危机会议](https://www.techmeme.com/260816/p10#a260816p10) ⭐️ 7.0/10

法国总理 Sebastien Lecornu 将于周一召开危机会议，回应法国税务机构在 6 月至 7 月间遭受的网络攻击，该攻击导致 67.8 万个个人和企业账户信息泄露。 此次泄露暴露了敏感的纳税人信息，并引发政府高层响应，凸显关键公共机构面临的网络安全威胁日益严峻，受影响个人和企业可能面临身份盗用或欺诈风险。 网络攻击发生在 6 月至 7 月，并于上周披露；受影响的包括个人和企业账户，但攻击途径或泄露数据类型等更多细节尚未公布。

rss · Techmeme · 8月16日 20:40

**背景**: 法国税务机构负责税收征管并掌握数百万个人和企业的敏感财务信息，因此成为网络攻击的高价值目标。危机会议通常会召集政府和安全部门高层，评估损失、协调响应并决定向受影响公民提供保护措施。

**标签**: `#cybersecurity`, `#data breach`, `#government`, `#France`, `#tax agency`

---

<a id="item-12"></a>
## [菲尔兹奖得主高尔斯：LLM 解数学难题多靠反例而非证明](https://www.techmeme.com/260816/p4#a260816p4) ⭐️ 7.0/10

蒂莫西·高尔斯在一篇博客中指出，迄今为止大语言模型解决著名数学问题，几乎都是通过给出反例而非证明。这显示出当前大语言模型在寻找反例方面表现更强，而在构造证明上较弱。 这一观察厘清了大语言模型在数学中的现有优势与局限，可引导研究者将其用于猜想检验和反例搜索。它还表明全自动定理证明仍是难题，影响人工智能工具在数学研究中的应用方式。 高尔斯特别提到“著名数学问题”，这意味着大语言模型的显著成果往往来自反例。博客标题“大语言模型擅长什么类型的数学？”也表明他在更广泛地评估其数学能力。

rss · Techmeme · 8月16日 06:00

**背景**: 蒂莫西·高尔斯是英国数学家，1998 年获得菲尔兹奖，以组合数学研究闻名。大语言模型是基于海量文本训练的 AI 系统，近期被用于数学推理任务，但在证明生成上表现参差不齐。在数学中，反例是能推翻一个普遍猜想的单个例子，而证明是对命题在所有情况下都成立的逻辑论证；通常找反例比证明定理容易得多。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLMs`, `#mathematics`, `#machine reasoning`, `#research commentary`

---

<a id="item-13"></a>
## [Hugging Face 称 Qwen 衍生模型超 15.1 万，成开放模型生态重要基础](https://www.techmeme.com/260816/p3#a260816p3) ⭐️ 7.0/10

Hugging Face 在 2026 年夏季《开放模型现状》报告中指出，开发者已基于阿里 Qwen 模型系列创建超过 15.1 万个衍生模型，数量居所有开放模型基础模型之首。 这巩固了 Qwen 作为开放模型生态中最大基础模型之一的地位，凸显开放权重模型格局向中国模型倾斜的趋势，对 AI 采用、竞争和开发者选择具有重要影响。 15.1 万以上的数字仅反映 Hugging Face 平台上的衍生模型；2026 年 8 月中旬《财富》的另一篇报道提到 Qwen 下载量达 30 亿次、生态衍生模型超过 30 万个，表明全平台总量可能更大。

rss · Techmeme · 8月16日 05:50

**背景**: Hugging Face 是重要的开源 AI 平台，开发者可在此分享模型和数据集。Qwen 是阿里云推出的开放权重大语言模型系列，在多个规模上表现优异。衍生模型是指对基础模型进行微调、合并或其他修改后产生的变体，常被用来衡量开放模型的采用程度。Hugging Face 每半年发布《开放模型现状》报告，跟踪相关生态趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fortune.com/2026/08/15/alibaba-qwen-open-ai-models-3-billion-downloads-meta-google/">Alibaba AI models hit 3 billion downloads, passing Meta... | Fortune</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face</a></li>

</ul>
</details>

**标签**: `#open-source AI`, `#Qwen`, `#Hugging Face`, `#model ecosystem`, `#derivatives`

---

<a id="item-14"></a>
## [Qwen3.8-27B 表现出色，但默认设置导致过度思考](https://simonwillison.net/2026/Aug/16/qwen-38-27b/) ⭐️ 7.0/10

Simon Willison 评测了阿里 Qwen 实验室发布的 Apache 2.0 许可、270 亿参数视觉语言模型 Qwen3.8-27B，发现其性能优秀，但默认推理力度 xhigh 会导致严重过度思考；例如生成一幅“骑自行车的鹈鹕” SVG 耗时 21 分钟，使用了 22,276 个推理 token。 对希望在笔记本上本地运行开源模型的用户来说，这一默认设置可能让适合消费级硬件的 27B 尺寸变得不实用；同时它也凸显了当前大模型在推理深度与速度/成本之间需要更好默认平衡的问题。 官方文档称默认 reasoning_effort 为 xhigh，LM Studio 的量化 GGUF 保留了该默认值；作者将上下文长度从 8,192 提升到 262,144 后才避免思考过程占满上下文，并在 128GB M5 Max MacBook Pro 和 NVIDIA DGX Spark 上使用 17GB Q4_K_M 量化版本进行了测试。

rss · Simon Willison Blog · 8月16日 22:00

**背景**: Qwen 是阿里巴巴旗下的开源模型系列；270 亿参数的稠密模型可在配置较好的本地硬件上运行，GGUF 是常用的量化格式，能显著减小体积。reasoning_effort 控制模型在回答前进行内部推理的 token 数量，推理过度会导致响应缓慢、成本上升但未必提升最终质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>
<li><a href="https://lmstudio.ai/models/qwen/qwen3.8-27b">qwen/qwen3.8-27b • LM Studio</a></li>
<li><a href="https://arxiv.org/pdf/2510.07880">Do LLMs Really Need 10+ Thoughts for "Find the Time 1000 Days..."</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#LLM`, `#AI`, `#Open Source`, `#Model Evaluation`

---

<a id="item-15"></a>
## [SSOG-Attention：可分离高斯和实现次二次注意力](https://www.reddit.com/r/MachineLearning/comments/1vpt6ay/ssogattention_sum_of_separable_gaussians_as_a/) ⭐️ 7.0/10

SSOG-Attention 提出一种新的注意力机制，用可学习的、由查询几何引导的高斯原子替代标准缩放点积注意力，将复杂度从 O(N²·d) 降至 O(N·√N·d)。该项目报告在 CIFAR-100 上优于 SDPA，在 ImageNet-1k 上性能相当且收敛更快。 该方法有望降低视觉 Transformer 等基于注意力模型的计算和内存开销，支持更长的序列或更大的图像。它属于次二次注意力研究，提供了一种可微分、类似核方法的替代方案，可能比全注意力更具扩展性。 SSOG 为每个头学习少量高斯原子，并将其分解为可分离高斯和，从而实现 O(N·√N·d) 复杂度。报告结果包括在 CIFAR-100 上优于 SDPA、在 ImageNet-1k 上性能相当且收敛更快；代码和博客为个人发布，使用了 AI 辅助，尚未经过独立验证。

reddit · r/MachineLearning · /u/4rtemi5 · 8月16日 10:06

**背景**: 标准缩放点积注意力（SDPA）在 Transformer 中计算每个查询与所有键之间的成对相似度，导致 O(N²·d) 成本。次二次注意力方法使用低秩、核或稀疏近似来避免全对全计算。SSOG 使用可分离高斯核之和：每个高斯原子可以分解为一次只依赖一个维度的因子，从而实现高效分解并降低复杂度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.pytorch.org/docs/2.13/generated/torch.nn.functional.scaled_dot_product_attention.html">torch.nn.functional.scaled_dot_product_attention — PyTorch 2. ...</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-sub-quadratic-sparse-attention-subq-ssa">What Is Sub - Quadratic Sparse Attention ? | MindStudio</a></li>

</ul>
</details>

**标签**: `#attention mechanism`, `#efficient transformers`, `#sub-quadratic attention`, `#machine learning`, `#computer vision`

---

<a id="item-16"></a>
## [线性注意力在 DNA 大海捞针回忆测试中失败](https://www.reddit.com/r/MachineLearning/comments/1vpqwdc/how_can_we_solve_longrange_recall_in_linear/) ⭐️ 7.0/10

一位 Reddit 用户报告，自定义线性注意力模型和 HyenaDNA 在 DNA“大海捞针”回忆基准上准确率仅约 25–27%，接近四字符 DNA 词表的随机水平。该用户正在寻找能够扩展到百万 token DNA 序列、且无需退回昂贵 softmax 注意力或大型外部记忆的架构方案。 这凸显了高效注意力机制在处理长基因组序列时的关键限制，因为标准 softmax 注意力计算成本过高。若能解决长程回忆问题，有望推动基因组学和其他长上下文任务的大规模基础模型发展。 DNA 序列可达 100 万 token，四字符词表下随机准确率为 25%；在 16K 上下文的小型线性注意力模型可达到 50–60%的回忆率，但随着上下文变长性能严重下降。现有方案包括外部记忆、滑动/近期 token 机制或线性与 softmax 混合注意力。

reddit · r/MachineLearning · /u/No-Coffee-8227 · 8月16日 07:47

**背景**: 线性注意力用核特征映射替代 softmax 相似度，将时间和内存复杂度从序列长度的二次方降为线性，但会把历史压缩为固定大小的状态，可能丢失精确的 token 级检索能力。HyenaDNA 是基于 Hyena 长卷积的基因组基础模型，在人类参考基因组上预训练，上下文长度可达 100 万 token。“大海捞针”基准测试模型能否从长上下文中检索到特定的“针”信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2306.15794">[2306.15794] HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution</a></li>
<li><a href="https://towardsdatascience.com/linear-attention-is-all-you-need-5fa9c845c1b5/">Linear Attention Is All You Need - Towards Data Science</a></li>
<li><a href="https://arize.com/blog/the-needle-in-a-haystack-test-evaluating-the-performance-of-llm-rag-systems/">The Needle In a Haystack Test: Evaluating the Performance... - Arize AI</a></li>

</ul>
</details>

**标签**: `#linear attention`, `#long-range recall`, `#DNA modeling`, `#efficient transformers`, `#needle in a haystack`

---

<a id="item-17"></a>
## [Firefox iOS 版新增内置广告拦截功能](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) ⭐️ 6.0/10

Mozilla 在 Firefox iOS 浏览器中加入了原生广告拦截功能，用户无需额外安装内容拦截扩展即可在应用内屏蔽广告。 这为 Firefox iOS 用户提供了内置的隐私保护和可能更快的页面加载，但由于 iOS 上已有 Firefox Focus 和 Safari 的 uBlock Origin Lite 等替代方案，其影响相对有限。它也反映出 iOS 平台对浏览器的限制（如必须使用 WebKit）仍在影响功能扩展和竞争格局。 根据用户讨论，内置拦截器可能不会移除 Google、Bing、DuckDuckGo 等搜索引擎结果页上显示的广告。Firefox iOS 版仍基于 WebKit，因此无法使用 Gecko 引擎，也无法像桌面版那样支持同样的扩展 API。

hackernews · pentagrama · 8月16日 12:58 · [社区讨论](https://news.ycombinator.com/item?id=49319633)

**背景**: 在 iOS 上，苹果要求所有浏览器使用 WebKit 渲染引擎，这限制了扩展功能。Safari 支持内容拦截器——这类应用或扩展提供过滤规则，但不会看到用户的浏览数据。Mozilla 的独立 iOS 浏览器 Firefox Focus 早已提供广告和跟踪器拦截，并能为 Safari 提供拦截规则。此前，主 Firefox iOS 浏览器并没有内置广告拦截器，用户需要安装外部内容拦截器或使用 Focus。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://webkit.org/blog/3476/content-blockers-first-look/">Introduction to WebKit Content Blockers | WebKit</a></li>
<li><a href="https://apps.apple.com/us/app/firefox-focus-privacy-browser/id1055677337">Firefox Focus: Privacy browser - App Store What is Firefox Focus for iOS? | Firefox Focus Help Firefox Focus: The privacy browser — Firefox.com Firefox Focus: Privacy browser for iOS (iPhone/iPad) - Free ... Download Firefox Focus (free) for Android, APK and iOS | Gizmodo Download Firefox for iOS — Firefox.com Firefox Focus: Privacy browser on the App Store</a></li>
<li><a href="https://support.mozilla.org/en-US/kb/focus">What is Firefox Focus for iOS? | Firefox Focus Help Firefox Focus: The privacy browser — Firefox.com Firefox Focus: Privacy browser for iOS (iPhone/iPad) - Free ... Download Firefox Focus (free) for Android, APK and iOS | Gizmodo Download Firefox for iOS — Firefox.com Firefox Focus: Privacy browser on the App Store</a></li>

</ul>
</details>

**社区讨论**: 评论观点不一：有人指出 Safari 的 uBlock Origin Lite 已经很好用，Firefox Focus 也早已提供类似拦截，因此这次更多是便利性提升。另一些人则对 iOS 的限制表示不满，例如无法使用 Gecko 引擎和扩展支持不足，并指出搜索结果页的广告可能仍会显示。

**标签**: `#Firefox`, `#iOS`, `#adblocking`, `#privacy`, `#browser`

---

<a id="item-18"></a>
## [AI 创造的新问题及人们的应对之道](https://podcasters.spotify.com/pod/show/nlw/episodes/The-New-Problems-AI-Is-Creating-And-How-People-Are-Solving-Them-e3nff4j) ⭐️ 6.0/10

这期 The AI Daily Brief 播客探讨了 AI 带来的新问题，包括 AI 垃圾内容、不断上涨的 token 成本、不均衡的生产率提升、劳动力技能退化以及人类专业知识流失，并讨论了个人和企业如何应对。 这些问题揭示了快速采用 AI 的副作用，影响内容质量、企业成本、员工技能和长期知识传承；理解应对措施有助于实现更可持续的 AI 整合。 该节目讨论了 AI 垃圾内容、token 成本治理、不均衡生产率、技能退化以及人类专业知识保护等话题，但没有提供具体案例或量化数据，技术深度有限。

rss · The AI Daily Brief · 8月16日 11:12

**背景**: AI 垃圾内容（AI slop）是指由生成式 AI 制作、质量低下且大量生产的数字内容，常用于吸引流量或牟利。Token 成本指 AI 模型处理输入和输出文本时产生的计算费用，如果管理不善会侵蚀 AI 投资回报。劳动力技能退化（workforce deskilling）发生在自动化减少了人类练习核心技能的机会时，再培训（reskilling）计划被认为可以缓解这一影响。节目还提出了在 AI 能力增强时如何保留人类专业知识的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_slop">AI slop</a></li>
<li><a href="https://www.volanea.com/blog/ai-token-costs-expensive-models-win">AI Token Costs : Why Expensive Models Still Win</a></li>
<li><a href="https://www.aihr.com/blog/reskilling/">Reskilling Your Workforce for the Future: An HR's Guide - AIHR</a></li>

</ul>
</details>

**标签**: `#AI`, `#podcast`, `#societal impact`, `#productivity`, `#workforce`

---

<a id="item-19"></a>
## [Face2Gene 等 AI 工具在罕见病诊断中应用增多](https://www.techmeme.com/260816/p8#a260816p8) ⭐️ 6.0/10

《华尔街日报》报道，患者、家属、医生和护士越来越多地使用 Face2Gene 等 AI 工具来识别罕见和难以诊断的疾病。Face2Gene 的 CLINIC 套件利用计算机视觉和深度学习，根据面部特征和人体测量数据提出综合征建议。 AI 辅助表型分析可能缩短许多罕见病患者漫长的确诊过程，帮助临床医生更早考虑罕见综合征。这也反映了 AI 在临床工作流程中的更广泛应用，有望改善诊疗，但仍需医生监督。 Face2Gene 定位为搜索和参考工具，而非诊断设备；其 CLINIC 套件基于面部特征和人体测量数据，利用计算机视觉、深度学习和 AI 提供综合征建议、注释和参考文献。

rss · Techmeme · 8月16日 17:30

**背景**: 罕见病通常难以诊断，因为单个临床医生可能见到的病例很少，且症状可能与常见病重叠。Face2Gene 是一套表型分析应用，可分析与遗传综合征相关的面部特征。它使用基于患者照片训练的深度学习模型生成综合征建议，但其结果旨在辅助而非取代临床医生的判断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.face2gene.com/">Home - Face2Gene</a></li>
<li><a href="https://www.face2gene.com/startclinic/">Getting Started with Face2Gene CLINIC - Face2Gene</a></li>

</ul>
</details>

**标签**: `#AI in healthcare`, `#medical diagnosis`, `#rare diseases`, `#machine learning`, `#technology adoption`

---

<a id="item-20"></a>
## [AI 与数据中心政策成美国中期选举重要议题，约四成选战提及](https://www.techmeme.com/260816/p7#a260816p7) ⭐️ 6.0/10

《华盛顿邮报》于 2026 年 8 月 14 日报道，人工智能与数据中心政策首次在美国中期选举中广泛出现，约 40%的选战候选人在其网站上提及相关议题。 这表明 AI 已从专业科技议题转变为主流政治议题，影响地方能源、就业、隐私和监管等讨论，候选人正在回应选民关切以及数据中心热潮带来的经济影响。 《华盛顿邮报》的分析发现，约四成美国选战的候选人在其竞选网站上提到 AI 或数据中心政策，但报道未详细说明具体政策立场或党派分布。

rss · Techmeme · 8月16日 15:20

**背景**: 美国中期选举是总统大选之间的国会及地方选举，通常聚焦本地议题。近年来 AI 迅速发展，数据中心作为算力基础设施，涉及大量电力、土地和就业，成为许多社区争议的焦点。AI 技术还引发隐私、就业影响和监管需求等关切，使得这些议题进入政治话语。

**标签**: `#AI policy`, `#elections`, `#midterms`, `#data centers`, `#US politics`

---

<a id="item-21"></a>
## [索尼 CEO 十时裕树推动公司向娱乐业务转型](https://www.techmeme.com/260816/p6#a260816p6) ⭐️ 6.0/10

《华尔街日报》发布了对索尼 CEO 十时裕树的专访，报道他计划将索尼从以电子业务为主转型为以音乐、电影、视频游戏及其支撑技术为核心的公司。 这一战略转型反映了硬件制造商优先发展内容与服务以推动增长的行业趋势。如果成功，可能重塑索尼在流媒体和游戏领域的竞争地位，并影响投资者、创作者和消费者。 该报道指出索尼曾以电子产品起家，但十时裕树表示未来属于娱乐业务；不过文章未披露具体财务目标或详细实施时间表。

rss · Techmeme · 8月16日 12:45

**背景**: 索尼公司成立于 1946 年，最初以 Walkman 随身听和特丽珑电视等消费电子产品闻名。后来通过收购 CBS 唱片和哥伦比亚影业以及推出 PlayStation，逐步扩展至音乐、电影和游戏领域。如今该公司业务涵盖游戏、音乐、影视和图像传感器，娱乐已成为重要利润来源。

**标签**: `#Sony`, `#corporate strategy`, `#entertainment`, `#technology`, `#business`

---

<a id="item-22"></a>
## [Pathway 获 3000 万美元种子轮，估值 5 亿美元，主攻后 Transformer 架构](https://www.techmeme.com/260816/p1#a260816p1) ⭐️ 6.0/10

据 Unite.AI 报道，AI 初创公司 Pathway 宣布种子轮融资总额达到 3000 万美元，估值 5 亿美元，用于扩展其称为“Post-Transformer”的 Baby Dragon Hatchling（BDH）架构。 这笔融资表明投资者对旨在克服标准 Transformer 局限性的后 Transformer 架构兴趣上升，可能推动更高效、更自主的 AI 系统发展。如果 BDH 的声明得到验证，它可能影响下一代大语言模型和实时 AI 应用。 Pathway 的 BDH 是一种受生物学启发的语言模型架构，旨在解决 AI 随时间泛化能力不足这一自主 AI 的关键障碍。本轮种子轮总额为 3000 万美元，估值 5 亿美元，但公告未提供详细技术基准或第三方验证。

rss · Techmeme · 8月16日 05:40

**背景**: 后 Transformer 架构指超越标准 Transformer 注意力机制的广泛研究方向，包括状态空间模型、世界模型和记忆增强网络，旨在实现更好的扩展性、长序列建模和推理能力。Pathway 的 BDH 是一个受生物学启发的语言模型架构例子，连接了深度学习和神经科学。该公司自称构建能像人类一样实时思考的“活 AI”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cacm.acm.org/news/beyond-llms-a-post-transformer-world-emerges/">Beyond LLMs: A Post-Transformer World Emerges – Communications of the ACM</a></li>
<li><a href="https://www.businesswire.com/news/home/20251001665931/en/Pathway-Launches-a-New-Post-Transformer-Architecture-That-Paves-the-Way-for-Autonomous-AI">Pathway Launches a New “Post-Transformer” Architecture That Paves the Way for Autonomous AI</a></li>
<li><a href="https://github.com/pathwaycom/bdh">GitHub - pathwaycom/bdh: BDH (Dragon Hatchling) – Architecture and Code</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#post-transformer`, `#deep learning`, `#startup`

---

<a id="item-23"></a>
## [中国民众对 AI 比美国更乐观，视其为低破坏工具](https://www.techmeme.com/260815/p18#a260815p18) ⭐️ 6.0/10

彭博社记者 Grace Shao 在 2026 年 8 月 14 日发表文章称，中国民众对人工智能的乐观程度显著高于美国人。这种差异源于在中国，AI 被视为一种实用工具，对人口的冲击比例小于美国。 这揭示了不同国家的技术经历如何塑造公众对 AI 的接受度，从而影响采用速度、监管和投资。理解这种态度差异有助于解释为何中国在公共服务和产业中部署 AI 时可能面临比美国更少的社会阻力。 现有摘录未提供具体的调查百分比或方法，而是将乐观度差距归因于不同的技术生活经历。其论点是，在中国，AI 被视为实用而非威胁，因此对人口的冲击比例较小。

rss · Techmeme · 8月16日 02:20

**背景**: 各国经常通过民意调查衡量公众对 AI 的乐观程度，此前研究显示态度差异与经济结构、岗位自动化风险和技术采用历史有关。在中国，AI 已融入移动支付、电商和人脸识别等日常服务，通常被宣传为便利工具。美国则更普遍担忧岗位流失、隐私和生成式 AI 对白领职业的影响。这篇文章通过比较这些经历来解释为何中国民众更乐观。

**标签**: `#AI`, `#society`, `#public perception`, `#technology adoption`, `#China`

---

<a id="item-24"></a>
## [SineKAN：使用正弦激活函数的柯尔莫哥洛夫-阿诺德网络](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 6.0/10

该帖子分享了一种名为 SineKAN 的柯尔莫哥洛夫-阿诺德网络变体，它用正弦激活函数取代 B 样条基函数，并附有 arXiv 论文（2407.04149）、GitHub 代码库和一篇 MDPI 同行评审论文。 KAN 正被探索作为传统 MLP 的更可解释替代方案，因此证明正弦激活能替代 B 样条可能简化实现，并为科学机器学习提供更平滑或更硬件友好的近似。 该研究记录在 arXiv:2407.04149，代码位于 github.com/ereinha/SineKAN，并在《Mathematics》13(19):3157 上经过同行评审；Reddit 帖子得分为 6.0，被描述为对现有 KAN 的渐进式改进。

reddit · r/MachineLearning · /u/jacobgorm · 8月17日 00:46

**背景**: 柯尔莫哥洛夫-阿诺德网络（KAN）是受柯尔莫哥洛夫-阿诺德表示定理启发的神经架构。与传统多层感知器不同，KAN 用可学习的单变量函数替代每个权重，该函数通常由 B 样条参数化。B 样条是具有最小支撑的分段多项式基函数，广泛用于曲线拟合和数值近似。SineKAN 将这些 B 样条替换为正弦激活函数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov-Arnold_Networks">Kolmogorov-Arnold Networks</a></li>
<li><a href="https://en.wikipedia.org/wiki/B-spline">B-spline</a></li>

</ul>
</details>

**标签**: `#Kolmogorov-Arnold Networks`, `#Sinusoidal Activation`, `#Neural Network Architecture`, `#Deep Learning`, `#Research Paper`

---

<a id="item-25"></a>
## [Riley Brown 使用 OpenAI Codex 运营百万粉丝内容业务](https://creatoreconomy.so/p/how-i-run-my-content-business-with-codex-riley-brown) ⭐️ 5.0/10

Riley Brown 分享了他的完整 AI 工具栈，说明如何利用 OpenAI Codex 为他拥有 150 多万粉丝的内容业务研究选题、撰写视频钩子并制作爆款缩略图。 这表明像 Codex 这样的 AI 编码智能体正被用于软件工程以外的领域，帮助个人创作者自动化内容生产中的创意和策略任务，可能推动内容行业更广泛地采用 AI 工具。 该内容强调 Codex 被用于选题研究、视频钩子和缩略图制作等非编程任务；根据维基百科，Codex 可通过 ChatGPT、命令行界面、桌面应用和多种 IDE 集成使用。

rss · Peter Yang (Behind the Craft) · 8月16日 14:03

**背景**: OpenAI Codex 最初是 2021 年推出的语言模型，在大量源代码上微调，用于将自然语言提示转换为代码。2025 年，OpenAI 将其重新定位为能够自主完成软件工程任务的 AI 编码智能体，并提供 ChatGPT、命令行界面、桌面应用和 IDE 扩展等多种使用方式。这则新闻显示创作者正在使用这一新的智能体版本来处理内容工作流，而非传统编程任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)">OpenAI Codex (AI agent) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Codex`, `#content creation`, `#YouTube`, `#automation`

---

<a id="item-26"></a>
## [马来西亚第二季度 GDP 增长 6%，受芯片制造和数据中心建设推动](https://www.techmeme.com/260816/p5#a260816p5) ⭐️ 5.0/10

根据《金融时报》报道，马来西亚第二季度 GDP 同比增长 6%，其中制造业增长 7.5%（受芯片制造驱动），建筑业增长 6.6%（受数据中心建设支撑）。 这一增长使马来西亚成为东南亚新兴的人工智能枢纽，全球 AI 热潮推动了对半导体和数据中心基础设施的需求，可能吸引更多科技投资并增强该国经济。 数据来自马来西亚第二季度 GDP 报告，制造业和建筑业是突出部门，芯片制造和数据中心建设是主要驱动因素。所提供摘要未包含具体的芯片制造商、数据中心项目或环比比较。

rss · Techmeme · 8月16日 09:45

**背景**: 马来西亚长期以来一直是电子制造以及半导体封装测试的重要基地，这使其能够从 AI 驱动的芯片需求激增中受益。数据中心是容纳服务器以支持云计算和 AI 工作负载的大型设施，其建设需要大量投资。东南亚正日益吸引寻求较低成本和战略位置的科技公司，马来西亚在这些领域的增长反映了这一趋势。

**标签**: `#AI`, `#semiconductors`, `#data centers`, `#Malaysia`, `#economy`

---

<a id="item-27"></a>
## [BlackBerry 实现 2017 年来首次 Q1 现金正增长，得益于 QNX 和 Secusmart](https://www.techmeme.com/260816/p2#a260816p2) ⭐️ 5.0/10

BlackBerry 报告本财年第一季度实现正向现金状况，这是自 2017 年以来首次在第一季度实现现金正向。公司将该结果主要归功于其 QNX 汽车软件和 Secusmart 安全通信产品。 这一里程碑验证了 BlackBerry 多年来从智能手机向汽车和安全软件转型的战略。它表明其嵌入式操作系统和安全通信业务正成为可持续的收入驱动力，这对投资者以及更广泛的汽车和网络安全行业都有影响。 QNX 是一种用于汽车和其他嵌入式系统的实时操作系统，Secusmart 主要面向政府客户提供防窃听移动通信解决方案。报道指出这是自 2017 年以来首个现金正向的第一季度，但 Techmeme 摘要中未披露具体部门财务数据。

rss · Techmeme · 8月16日 05:45

**背景**: BlackBerry 曾是主要的智能手机制造商，后来退出了手机业务，专注于企业软件和网络安全。QNX 是一种商业 Unix 类实时操作系统，广泛用于汽车信息娱乐和安全系统。Secusmart 是 BlackBerry 的德国子公司，专门为政府机构提供安全移动通信和防窃听技术。这两条产品线是 BlackBerry 当前汽车和安全软件市场战略的核心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/QNX">QNX</a></li>
<li><a href="https://de.wikipedia.org/wiki/Secusmart">Secusmart – Wikipedia</a></li>
<li><a href="https://www.linkedin.com/company/secusmart">Secusmart - LinkedIn</a></li>

</ul>
</details>

**标签**: `#BlackBerry`, `#QNX`, `#Secusmart`, `#automotive software`, `#financial results`

---

<a id="item-28"></a>
## [应届生寻求物理 AI 与机器人职业指导](https://www.reddit.com/r/MachineLearning/comments/1vq3p9w/career_advice_finalyear_in_physical_ai_robotics/) ⭐️ 5.0/10

一位印度高校大四本科生在 Reddit 机器学习版发帖，介绍了自己在跨国公司物理 AI 实习中使用 NVIDIA Isaac Sim 和 OpenFOAM 的经历，并就初级岗位招聘、国际机会和技能差距寻求建议。 该帖子反映了学生对物理 AI 和机器人职业日益增长的兴趣，但本身不提供技术洞见；意义主要在于引发关于新兴领域初级岗位招聘和所需技能的社区讨论。 帖子列出了 Isaac Sim、Gazebo、ROS/ROS 2、PX4、VIO、SLAM、Nav2 和强化学习等技能，并询问在最后一年应重点补充哪些框架或技能；帖子评分为 5.0/10，未包含评论。

reddit · r/MachineLearning · /u/avianbob · 8月16日 17:53

**背景**: 物理 AI 指将 AI 模型与传感器、执行器和机器人结合，在物理世界中进行感知、推理和行动的系统；NVIDIA Isaac Sim 是构建在 Omniverse 上的机器人仿真平台；OpenFOAM 是开源计算流体动力学工具箱。这些工具常用于机器人和自动驾驶开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Physical_AI">Physical AI</a></li>
<li><a href="https://developer.nvidia.com/isaac/sim">NVIDIA Isaac Sim</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenFOAM">OpenFOAM</a></li>

</ul>
</details>

**标签**: `#physical AI`, `#robotics`, `#career advice`, `#job market`, `#machine learning`

---