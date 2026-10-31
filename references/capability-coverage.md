# 请求—能力—证据覆盖

“方法”表示由宿主Agent按文档执行；“工具”表示仓库有可运行检查；它们都不代表已经完成未来论文的工作。

| 反复出现的具体要求 | 位置 | 形式/验收 |
|---|---|---|
| Agent领域具体问题、工程价值、最近邻和增量 | review-design | 方法；提案能说明新增认识 |
| 不因有人做过就否定，先理解局限 | review-design/search-and-evidence | 方法；具体条件逐项对比 |
| 期刊规定、报告指南、实施方法和博主经验分层 | method-authority、sources、worksheet | 方法；来源、日期、读取范围及适用对象，PRISMA不作实施质量证明 |
| 真实筛选者、独立性和AI参与 | method-authority、search-and-evidence | 方法；实际过程可追溯，不虚构独立人工 |
| 综述类型和目标期刊一起选 | review-design | 方法；类型/范围/同刊参考有记录 |
| 免费优先、低费备选、东南亚/新刊也核实 | review-design、worksheet | 方法；按费用/范围/索引事实评估，不按地区猜易录用 |
| 区分投稿/审稿/APC/可选OA与周期 | review-design、worksheet | 方法；来源、币种、日期、未知明确 |
| 原始论文、综述、代表作与最新材料 | search-and-evidence | 方法；原文深度与时间边界 |
| 检索失败、纳排、报告族、版本、未取全文 | search-and-evidence | 方法；真实执行日志与单位 |
| 数据和结论一一对照 | search-and-evidence、structure-and-synthesis | 方法；主张有原文位置 |
| 最后新增文献会不会改变结论 | search-and-evidence、lessons | 方法；批次综合对照 |
| 每章、每节、每段逻辑图 | structure-and-synthesis、worksheet | 方法；段落功能与证据/承接 |
| 学同领域、同类型和跨期刊综述的逻辑与表达 | writing-and-bilingual、worksheet | 方法；来源位置→功能/句法/术语→采用原则，不抄句或移植事实 |
| 起草时同步管语法、术语、逻辑与自我防御 | writing-and-bilingual、structure-and-synthesis | 方法；逐段局部检查、逐节衔接，准确术语和必要限定保留 |
| 动作/复合修饰/术语/上下文五项表达自测 | writing-and-bilingual、review-and-submission、worksheet | 方法；指出隐藏操作或证据缺口，保留领域术语、必要修饰和有定义的新概念，不按连字符/删词配额或AI率验收 |
| 清除不同句式的叠加防御与悬空转折 | writing-and-bilingual、structure-and-synthesis、review-and-submission | 方法；实际主张/新增信息/当前位置/承接判据，内部自检与正文分离，不按词表或全删否定 |
| 完稿后再严格审查并修复遗漏 | review-and-submission、worksheet | 方法；全文及派生件联查，已改与复核关闭分开，绑定最终版本 |
| 真实成稿测试与假阳性校准 | review-and-submission、writing-and-bilingual | 方法；精确位置/摘录、分级、待核语义、保留反例及真实覆盖；无缺陷配额 |
| 表格简写保留端点条件和行单位 | structure-and-synthesis | 方法；对象/触发点/排除/分母与正文一致，来源指标及定位明确 |
| 润色、去模板感、去无信息防御句 | writing-and-bilingual | 方法；语义保留，不按禁词表 |
| 英文主稿与对应中文翻译 | writing-and-bilingual | 方法；否定/条件/数字/范围同步 |
| 图号、文字、数据、正文引图一致 | figures-and-artifacts | 方法；真实源数据与图对应 |
| SVG真正可编辑、源与导出 | figures-and-artifacts | 方法；查看文本/路径与实际图 |
| Word/PDF能打开且实际版面正确 | figures-and-artifacts | 方法；真实渲染检查，不以文本提取代替 |
| 正文引用与参考文献跳转/支持 | figures-and-artifacts | 方法；身份、支持、联动三层 |
| S1–S4或类似资料包对照正文 | figures-and-artifacts、worksheet | 方法；按实际期刊命名，不强制S编号 |
| 作者页、贡献、经费、冲突、数据可用性 | review-and-submission | 方法；真实事实，不自动分配完成角色 |
| 私有草稿/审稿访问/公开许可分开 | review-and-submission | 方法；权限和实际状态一致 |
| AI说明逐位置、只按适用政策准确写 | review-and-submission | 方法；官网来源、用途和原文逐项 |
| 多余聊天标记/水印/制作说明清理 | figures-and-artifacts | 方法；保留合法引用和准确披露 |
| 查重与AI率给真实数值 | writing-and-bilingual、check_review.py | 工具仅核报告/哈希/范围；检测由外部服务执行 |
| 所有最新上传文件逐个给，不只ZIP | figures-and-artifacts、worksheet | 方法；逐项路径/哈希/用途 |
| 一个有效原文、归档旧版后清理冗余 | figures-and-artifacts | 方法；不删提交证据和别的任务 |
| 内容总审在提交前，而不是提交后 | review-and-submission、check_review.py | 方法+工具；全审证据及当前稿哈希 |
| 同上下文自审不冒称独立专家 | review-and-submission | 方法；如实记录来源 |
| 每一步监控技能走偏并反省 | lessons | 方法；决策、证据、产物、下一步 |
| 确认结果，不把计划当完成 | check_review.py、lessons | 工具+方法；passed需实际文件证据 |
| 不把提交/技术检查/外审/录用混淆 | review-and-submission、check_review.py | 工具核回执记录，实际阶段来自门户 |
| 不与并行任务混用文件和结论 | SKILL、figures-and-artifacts | 方法；当前任务边界和文件所有权 |
| 不无限验证、调到赢或堆文档 | review-design、lessons | 方法；预算/停止/重开条件 |

本轮没有把任何任务要求解释成必须购买服务、必须双人标注、必须调用多个Agent、必须模拟实验或必须公开论文。

## 本次能力整合增量

| 具体请求 | 实施位置 | 可观察产物 |
|---|---|---|
| 先研究综述方法/整合skills，领域写作停住 | SKILL、skill-adapters | 来源/许可/采用与舍弃矩阵，交付后不自动推进领域 |
| 从笔记走到新综合 | conduct-and-synthesis、structure-and-synthesis | 概念定义/单位、条件冲突、推导与边界 |
| 匹配单人资源和具体方法承诺 | method-authority、conduct-and-synthesis | 实施版本/团队要求/实际执行或偏离 |
| 排查检索策略和覆盖盲点 | search-and-evidence、conduct-and-synthesis | 平台语法、概念块、已知关键论文调试，真实搜索记录 |
| 核当前期刊政策差异 | journal-policy-profiles、review-and-submission | 用途/规则/位置/日期/未知卡，选刊时刷新 |
| 索引失败、版本差异与论断核验 | search-and-evidence | 身份/版本/支持状态分开，partial保留 |
| 跨文献图表和语义依赖 | figures-and-artifacts、writing-and-bilingual | 来源/节点边、数值角色、限定关系和联动检查 |

公开skill与本机能力只是来源和可选协作，不是安装清单、执行承诺或质量认证。
