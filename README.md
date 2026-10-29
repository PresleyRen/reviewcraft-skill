# ReviewCraft · 综述工坊

把“找文献、整理材料、写成文章”连接成一条能检查、能复用的综述工作流。

ReviewCraft提供一个可安装的Agent Skill，配套方法手册、逐段写作模板、审查与投稿检查，以及一个不联网的文件/状态检查器。它支持先研究综述方法与能力，再按用户选择进入具体领域。方法入口区分期刊规定、报告指南、研究实施和教授/博主经验，帮助为具体综述选择适用要求。它从实际综述任务中提炼经验，适合Agent、LLM、软件工程等领域；换领域时调整问题和证据标准。

## 能帮你完成什么

| 任务 | 产出 |
|---|---|
| 判断综述是否值得写 | 研究问题、最近邻综述差异、读者将得到的新认识 |
| 选目标期刊 | 核验综述类型、范围、费用、OA/Subscription、分区来源与年份、周期及投稿材料 |
| 从原文建立证据 | 检索、筛选、报告族、读取深度、定位与未知项 |
| 把材料变成综合 | 横向比较、冲突解释、适用边界、可追溯的工程建议 |
| 规划全文和每一段 | 主线图、章节过渡、段落功能、证据和下一段关系 |
| 学习并运用学术表达 | 从同领域、同类型的跨刊综述建立表达依据与术语表，起草时逐段检查语法、搭配、逻辑和无信息防御 |
| 同步中英文 | 英文为正式主稿时，中文忠实跟随；检查否定、条件、数字和范围 |
| 准备图表与文件 | 可编辑SVG、图号/引文对应、Word/PDF实际渲染、附件和哈希清单 |
| 完稿总审与投稿准备 | 写完再严格审一次全文，检查表格压缩是否丢条件、原生指标和实际行单位；分级记录问题、保留反例及语义待核项，再核对投稿材料 |
| 记录检测状态 | 查重与AI检测分别记录；没有报告就没有百分比 |

## 从哪里开始

```text
问题与读者需求 + 最近邻综述 + 目标期刊
  → 确定综述类型、范围、纳排和阅读预算
  → 执行检索 → 去重/报告族 → 筛选 → 原文提取
  → 跨文献综合 → 检查新增文献是否改变结论
  → 参考综述表达依据/术语 → 全文逻辑图 → 边写边检查段落 → 英文主稿
  → 图表/引文 → 中文同步 → 实际渲染
  → 审稿人总审 → 修改 → 复核
  → 检测状态与期刊要求核对
  → 冻结文件 → 授权上传/提交 → 保存真实回执
```

已有稿件直接进入当前阶段。无需为了用Skill把已经做完的工作重新做一遍。

## 安装与使用

要求：能读取Markdown技能的Agent；本地检查器与测试使用Python 3.10+标准库，不需要GPU、API密钥或付费检测账户。

在Codex中安装（目标目录不存在时执行）：

```sh
git clone https://github.com/PresleyRen/reviewcraft-skill.git "$HOME/.codex/skills/reviewcraft"
```

如果Codex使用自定义技能目录，改用自己的目录。安装后按客户端实际加载方式重新载入技能。其他支持本地`SKILL.md`的客户端可以使用本仓库内容，但未逐一验证各客户端的自动发现机制。不要在重复安装时覆盖已有修改。

示例请求：

> 用 $reviewcraft 评估这个综述问题，与三篇最近邻综述和目标期刊要求对照。先给我值得写的理由、已有内容和具体新增综合，别只列目录。

> 用 $reviewcraft 读取现有综述和证据表，先画全文与每段逻辑，再逐段检查结论、引文、重复和表达。修改后同步中文并查看实际PDF。

> 用 $reviewcraft 做投稿前总审，给出原文位置、证据、作者能作出的最强回应、最小修改和关闭条件。未完成的检查不要写成通过。

> 用 $reviewcraft 准备期刊附件，核对最新文件身份、作者声明和目标期刊要求。没有实际查重/AI报告就明确记为未检测，停在我授权的阶段。

## 本地工具：防止“检查过旧稿，却提交了新稿”

复制[状态模板](templates/project-state.json)到自己的研究目录，填写真实文件与检查证据。模板默认不通过，要求把实际未做的工作保留下来。

```sh
python3 scripts/check_review.py --root /path/to/my-review --state project-state.json
python3 -m unittest discover -s tests -v
python3 scripts/check_review.py --root examples/synthetic-review --state project-state.json
```

最后一个命令检查仓库自带的**合成示例**，预期成功；它不包含真实论文、检测报告或真实投稿。检查器会阻止缺文件、哈希不符、旧稿审查、没有证据的“通过”、缺报告的检测分数、超出配置阈值的报告和越界路径。

技能格式校验使用Skill Creator提供的`quick_validate.py`，它需要PyYAML。开发依赖锁定在[requirements-dev.txt](requirements-dev.txt)，可安装到仓库自己的环境；本地文件/状态检查器仍只用Python标准库：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python /path/to/skill-creator/scripts/quick_validate.py .
```

最后一行替换为自己已安装的Skill Creator校验脚本路径。格式校验通过确认技能入口结构有效；真实稿件的语法、术语和逻辑仍须按写作与审查模块实际阅读。

检测服务没有统一的强制阈值。项目有要求才设置`required`和`threshold_percent`；未要求的检测可以明确记为未请求，不虚构一次检测。脚本不生成检测分数，也不把低AI分数解释成真实作者身份或学术质量。

## 方法、代码与人工判断怎么分工

- **Skill**负责恢复状态、选阶段、调用适用方法、保存证据并交付结果。
- **手册与模板**提供选题、检索、综合、结构、表达、图表和投稿的具体工作办法。
- **检查器**负责文件与状态的确定性检查；科学支持、语义、视觉和实际政策理解由执行者核对。
- **外部系统**才能提供正式检测报告和投稿回执；仓库不自带这些权限和结果。

已有ClearWeave、Paper Review Atlas、FigureFoundry或文档/PDF工具时可以配合使用。ReviewCraft负责连接整个综述过程，不复制这些项目的实现，也不要求安装它们。

## 这次经验带来的关键修正

1. 将最终审稿人总审放在正式提交前，并绑定稿件哈希。
2. 将语言润色、查重和AI检测列为三个不同状态；不再用“已润色”代表“检测通过”。
3. 阅读预算停止后检查结论是否稳定，不把披露局限当作已经消除局限。
4. 抽样复核同时记录对象、字段、发现及处理；追加文献不能自动继承旧抽样的可靠性。
5. 先说新增综合带来什么判断，再写分类名和目录。
6. 只保留一个当前主稿，修改同步到实际受影响的中文、图注、附件和导出；提交源按回执冻结。

完整方法：[实施与综合](references/conduct-and-synthesis.md) · [相关skills整合](references/skill-adapters.md) · [期刊政策差异](references/journal-policy-profiles.md) · [方法与规范层级](references/method-authority.md) · [能力覆盖](references/capability-coverage.md) · [设计](references/review-design.md) · [检索证据](references/search-and-evidence.md) · [写作结构](references/structure-and-synthesis.md) · [表达与双语](references/writing-and-bilingual.md) · [图表文件](references/figures-and-artifacts.md) · [审查投稿](references/review-and-submission.md) · [经验](references/lessons.md) · [来源](references/sources.md)。

## 公开范围与许可

MIT许可适用于本仓库原创说明、模板和代码。链接指向的论文、政策和其他技能仍适用各自版权/许可；这里没有复制其完整实现或第三方论文全文。

仓库发布通用方法和合成示例。未发表稿件、中英文正文、真实作者资料、私有审稿链接、账户信息、投稿附件和原始研究日志不随本仓库公开。任何实际项目资料的发布仍按其权限和许可单独处理。

发布前的实际测试结果见[验证记录](VALIDATION.md)。本仓库不承诺录用、消除所有错误或达到某个检测百分比。
