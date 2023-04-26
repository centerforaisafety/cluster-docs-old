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
Grantees are only permitted to use the CAIS compute cluster to work on pre-approved projects. Each grantee is able to add research collaborators for these projects, who are then also able to access the compute cluster. The primary investigator (PI) is initially allowed to add up to 4 collaborators, with any further additions subject to approval by CAIS staff. It's important to note that PIs share the same slurm priority as their collaborators.

#### Time-Limited Access
Grantees given time-limited access to the cluster will have a limited number of GPU-hours for their experiments. After finishing, the grantee will be expected to fill out a brief report.

#### Project-Based Access
Grantees with project-based access to the cluster are not limited in the number of GPU-hours they can use. They will have unlimited cluster access until their project finishes or at most for a year, during which CAIS staff will conduct email check-ins with the PI every three months.

In the case that a project undergoes significant pivoting, you must let us know. We will review the project again. If no restrictions on pivoting are in place, project-based access would be equivalent to that of general access, which is not our intention.

At the end of the year, PIs must complete a more comprehensive report to renew their access to the cluster. Renewals will be assessed based on the safety-relevance of previous work and the research output.

### Job Allocation
The CAIS compute cluster uses slurm to allocate jobs. Jobs are subject to a hard limit of 48 hours, and if a longer run is necessary, please message CAIS staff to schedule this. Approval is granted on a case-by-case basis. Additionally, slurm's scheduling algorithm deprioritizes runs which require many GPUs. If a job is not reaching the top of the priority queue, feel free to reach out to CAIS staff. As before, approval will also be granted on a case-by-case basis. Once approved, the job will be scheduled for several days down the line.

During periods leading up to conference deadlines, the compute cluster is expected to experience high demand. It may be difficult or impossible to reserve GPUs in advance during these periods. As such, compute priority may solely be determined by slurm during these weeks.

### Project Scope
Grantees can only use the CAIS compute cluster for pre-approved research projects that focus on ML safety. A larger document outlining the research directions that fall within the scope of this program versus those that do not will be released soon.

If a grantee wishes to work on a new research project, they must submit the project for approval by CAIS staff through [this form](https://airtable.com/shrN5XbLE9oBIWVP8). CAIS staff will then follow-up with any additional questions or instructions. Any individual who is found to be using the compute cluster for a project that falls outside of the pre-approved research directions will face temporary or permanent suspension of their access to the cluster.

### Credit
If you use the CAIS compute cluster for your project, we kindly ask that you include the following statement in your paper's acknowledgements section.

    “This research was supported by the Center for AI Safety Compute Cluster. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the sponsors.”

Please note that by using the compute cluster, you agree to have your group or your paper featured on our website (where it clearly indicates that we merely supported the research and are not responsible for your work).

### Bugs and Feedback
Bugs should be reported in the #help-desk channel on the slack. General feedback about the cluster can be reported in [this form](https://airtable.com/shrqbKfS2KywKjhQS). For anything urgent, time sensitive, or possibly private please contact Steven Basart and Andriy Novykov directly on slack. (This way it notifies both of them.)
