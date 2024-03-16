---
layout: page
title: CAIS Compute Cluster Policies
---

- toc
{: toc }

### Quick Links
[New Project Approval Form](https://airtable.com/shrN5XbLE9oBIWVP8)  
[Feedback Form](https://airtable.com/shrqbKfS2KywKjhQS)

### Compute Access
Grantees are only permitted to use the CAIS Compute Cluster to work on pre-approved projects. Each grantee is able to add research collaborators for these projects, who are then also able to access the compute cluster. The primary investigator (PI) is initially allowed to add up to 4 collaborators, with any further additions subject to approval by CAIS staff. PIs share the same priority as their collaborators for scheduling jobs in SLURM.

### Project-Based Access
Grantees with project-based access to the cluster are not limited in the number of GPUs or GPU-hours they can use. 

We ask applicants submitting new projects or requesting extensions to indicate how long they expect to need for their project. By default, we encourage users to request access until one of the three annual review points for research updates and extensions. These review points occur roughly in early February, June and October, timed to take place after major conference submission deadlines (i.e. after ICML, NeurIPS, ICLR deadlines). Applicants can request access up to two review points away (up to the next review point or the one after that), meaning that they would have access for either one or two 4-month periods. They may later request an extension if further time is needed.

Applicants may also specify a shorter time period if only short-term access is needed.

At each review point (after ICML, NeurIPS, ICLR deadlines), PIs will be requested to provide an update on their research, which must be completed to maintain their access to the cluster. 

When the initial period requested by a user expires, we will invite them to apply to extend their existing project or submit a proposal for a new project. This will take into account the strength of the project proposal and the team's prior research output while using the cluster.

### Limited Access
Grantees with limited access to the cluster are allowed to use the "single" and "interactive" nodes. This is typically granted to users that are taking part in training programs or other early-career researchers. Other access conditions are similar to grantees with project-based access.

### Job Allocation
The CAIS compute cluster uses SLURM to allocate jobs. Jobs are subject to a hard limit of 48 hours, and if a longer run is necessary, please message CAIS staff to schedule this. Approval is granted on a case-by-case basis. SLURM's scheduling algorithm deprioritizes runs which require many GPUs. If a job is not reaching the top of the priority queue, feel free to reach out to CAIS staff. As before, increased priority to run jobs may be granted on a case-by-case basis. 

During periods leading up to conference deadlines, the compute cluster is expected to experience high demand. It may be difficult or impossible to reserve GPUs in advance during these periods. As such, compute priority may solely be determined by SLURM during these weeks.

### Project Scope
Grantees can only use the CAIS compute cluster for pre-approved research projects that focus on ML safety. Any individual who is found to be using the compute cluster for a project that falls outside of the pre-approved research directions will face temporary or permanent suspension of their access to the cluster.

For a non-exhaustive list of topics we are excited about, see Unsolved Problems in ML Safety or the Intro to ML Safety Course. We may also consider other research areas provided appropriate justification of the impact on ML safety is provided. We are particularly excited to support work on LLM adversarial robustness and transparency. 

Work which improves general capabilities or work that improves safety as a consequence of improving general capabilities are not in scope. “General capabilities” of AI refers to concepts such as a model’s accuracy on typical tasks, sequential decision making abilities in typical environments, reasoning abilities on typical problems, and so on.

If a grantee wishes to work on a new research project, they must submit the project for approval by CAIS staff through the application form linked on CAIS' website (https://www.safe.ai/work/compute-cluster). 

### Credit
If you use the CAIS compute cluster for your project, we kindly ask that you include the following statement in your paper's acknowledgements section.

    “This research was supported by the Center for AI Safety Compute Cluster. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the sponsors.”

Please note that by using the compute cluster, you agree to have your group or your paper featured on our website (where it clearly indicates that we merely supported the research and are not responsible for your work).

### Bugs and Feedback
Bugs should be reported in the #help-desk channel in the cluster's Slack workspace. General feedback about the cluster can be reported in [this form](https://airtable.com/shrqbKfS2KywKjhQS). For anything urgent, time sensitive, or possibly private please contact Andriy Novykov directly on Slack.
