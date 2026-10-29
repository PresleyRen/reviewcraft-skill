# 相关skills：能力整合与来源

在研究综述能力、扩展本skill或选择可选协作者时使用。2026-10-29有界审读了8个公开仓库的15个入口，以及12个相关本机skill快照。公开市场没有完整统一名录；未宣称穷尽。这里只保存有用操作及来源，未复制上游skill文字、模板或脚本，也不引入安装/付费/定时/外发动作。

## 公开来源的采用与舍弃

链接固定到本轮commit；同仓库多个入口不是独立方法证据，衍生版本也不重复计数。入口/许可审读不是整个仓库的运行安全或科学效果验证。

| 来源/版本/许可 | 已读入口 | 接入ReviewCraft的能力 | 不继承的假设/流程 |
|---|---|---|---|
| [K-Dense](https://github.com/K-Dense-AI/scientific-agent-skills/tree/5f2bc0341354fd5590aef76a533ada1e1e5b4e62)，MIT | literature-review、citation-management、research-lookup、scientific-writing；core_workflow | 搜索/报告/研究单位、失败记录、反证检索、版本与论断支持分查 → search-and-evidence / conduct-and-synthesis | 固定引用数、付费后端、强制额外账本与图生 |
| [pinshuai](https://github.com/pinshuai/literature-review-skill/tree/ed62a2899202707b58e87e4cd6ae45792772fe58)，MIT，K-Dense衍生 | SKILL | 查询轮次/引用渲染检查 → search-and-evidence / figures-and-artifacts | 固定篇数/库数、声望筛选、个人路径、全局安装 |
| [xingtaxueshu](https://github.com/xingtaxueshu/literature-review-skills/tree/177bec5b5187f6016a24df9c388cd5e0a88ce792)，MIT | map-literature-contradictions、compare-research-methods；source-integrity | 条件层矛盾及证据设计能回答什么 → conduct-and-synthesis | 固定社会科学类别、把用户提供当核验、强制输出格式 |
| [ShaishavMaisuria](https://github.com/ShaishavMaisuria/research-paper-lifecycle-skills/tree/cf30d6452cc6fd0570dd760eb65696f4a3485398)，Apache-2.0 | draft-survey、verify-citations；triage-guide | survey/related-work区别、索引故障/版本/更正核验 → conduct-and-synthesis / search-and-evidence | 引文排行决定纳入、固定页数、第二memory系统 |
| [ByteDance DeerFlow](https://github.com/bytedance/deer-flow/tree/b537d9c16c84e432ee609da57f042d4926c94f8c)，MIT | systematic-literature-review | 按资源分批提取、失败批次保留、跨文献比较 → search-and-evidence / structure-and-synthesis | arXiv单查询等于系统覆盖、不存查询结果、特定runtime强制多Agent与论文上限 |
| [YANZHANLIN](https://github.com/YANZHANLIN/literature-review-skill/tree/7328261b9274e8647ab017a0f94a98281702ce82)，MIT | 根路由、文献综述写作 | 独立综述/学位章/Related Work分路；概念矩阵 → conduct-and-synthesis | 未校准评分门、统一篇幅/语言比例、把全部全文获取设成通用条件 |
| [stephenlzc](https://github.com/stephenlzc/AI-Powered-Literature-Review-Skills/tree/b4e4c7e8834993fa517927fe6c57978192e64c21)，MIT | SKILL | 大纲→草稿→定位审查→修订闭环 → structure-and-synthesis / review-and-submission | 固定语料配额、DOI格式当核验、任意质量分与“可直接投稿”模板 |
| [lingzhi227](https://github.com/lingzhi227/agent-research-skills/tree/9e6c085d65e313e475e921fdfe795ac11eb7589e)，当前树未发现LICENSE | literature-review、survey-generation | 多视角问题、章节证据检索、相邻章节连贯性 → search-and-evidence / structure-and-synthesis | 角色模拟当专家、固定篇数/字数、引用量筛选、NLI当最终支持证明；只参考思想，不转载 |

## 本机已有能力的衔接

| 能力来源 | 采用原则/放入何处 | 复用限制 |
|---|---|---|
| ScholarRoute / Agent Research Atlas | 阶段路由、最近邻/反证和决定导向阅读 → review-design / conduct-and-synthesis | 不建立第二套atlas/CLI。Atlas部分Supervisor参考和模板有CC BY-NC-SA许可，未复制 |
| Paper Review Atlas | 作者侧挑战→保留/缩小/撤回→实际关闭 → review-and-submission | 不强制问题数量或模拟报告数量 |
| ClearWeave | 数字角色、条件依赖、归属与确定性保存 → writing-and-bilingual | 不引入禁词表或检测分数承诺 |
| FigureFoundry | 图要回答的问题、证据与解释分开、实际查看 → figures-and-artifacts | 编辑性/导出按用途，不把所有图强制为一种格式 |
| nature-academic-search / nature-citation | 可用工具路由、分段论断支持、元数据导出 → search-and-evidence | 列出的工具须实际可用；不继承CNS-only/MeSH默认范围 |
| nature-literature-pipeline | 多ID去重、读取深度/版本 → search-and-evidence | 不继承声望加权、top-k、cron或外发；日常发现不等于综述纳入 |
| nature-reader | 页/节/块/图表定位 → conduct-and-synthesis | 不强制全部论文做双语全文reader |
| nature-writing / nature-polishing / nature-reviewer | 先论证后语言、恢复共享事实、按范围审查 → structure / writing / review | 不继承统一Nature格式、固定三报告或源名当权威 |

本机快照不能代表最新远端；多数安装目录没有可核的顶层许可。这里只整合独立表达的通用操作，并保留可选协作入口。未来确需复制任何实质文字/代码时，先核其具体文件许可并保留通知；开放许可不证明方法有效。

## 新增来源怎么继续接入

对新skill先问：它提供什么现有模块没有的可观察能力？实际读了哪些文件/commit？需要什么工具、数据、成本和授权？是否与当前方法/期刊冲突？采用哪一项，舍弃哪一项，怎样用真实场景核验？

将操作映射现有模块；只有出现独立且必要的新能力才新增模块。优先用原始方法/官方规则核对建议，不以安装量、星数、市场安全徽章或模型评分决定采用。用户明确暂停领域推进时，方法研究/skill完善完成后停在交付，不自动转入新领域检索或正文写作。
