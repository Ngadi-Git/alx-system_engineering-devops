# Postmortem

This postmortem serves to identify the root cause of the API infrastructure outage and outlines corrective and preventative measures to prevent similar incidents in the future. By implementing these actions, we aim to ensure the continued reliability and performance of our critical API infrastructure.

## Issue Summary:
* **Duration:** The API infrastructure outage occurred on Friday, March 8th, 2024, from 7:15 PM GMT to 10:30 PM GMT (1:15 PM PST to 4:30 PM PST).
* **Impact:** All internal and external applications relying on our APIs experienced significant slowness and intermittent failures. Approximately 80% of user traffic was affected. Users were unable to complete tasks or received error messages.
* **Root Cause:** A configuration change deployed during a scheduled database maintenance window inadvertently triggered a cascading series of errors that overloaded the API gateway.

## Timeline

* **7:15 PM GMT:** Monitoring alerts indicated a surge in API request latency and error rates.
* **7:20 PM GMT:** On-call engineer identified the issue through monitoring dashboards and confirmed widespread API failures.
* **7:20 PM - 8:00 PM GMT:** The engineering team investigated potential causes, initially focusing on the database maintenance window as the most likely culprit.
* **8:00 PM - 9:00 PM GMT:** Investigation into the database revealed no anomalies. Engineers then shifted focus to the API gateway, suspecting a resource bottleneck.
* **9:00 PM - 9:30 PM GMT:** A code review of the recently deployed configuration changes identified an error that was causing the API gateway to process requests inefficiently.
* **9:30 PM GMT:** The incident was escalated to the SRE (Site Reliability Engineering) team for a coordinated rollback of the faulty configuration.
* **10:00 PM GMT:** The configuration change was successfully rolled back, and API functionality began to recover.
* **10:30 PM GMT:** API performance returned to normal levels, and all services were fully operational.

## Resolution
- A scheduled database maintenance window included a configuration change intended to optimize database performance.  However, due to a human error in the configuration script, the API gateway received requests in an unexpected format. This overwhelmed the gateway's processing capabilities, causing it to queue and backlog requests, leading to the observed slowness and errors.

- The resolution involved identifying the faulty configuration script and reverting it to the previous version. This restored the API gateway's  ability to handle requests efficiently.

## Corrective and Preventative Measures:

* **Improve code review processes:** Implement a more thorough code review process with a focus on configuration changes, especially those deployed during maintenance windows.
* **Automated Testing:** Develop automated tests for API gateway configurations to identify potential issues before deployment.
* **Monitoring Enhancements:** Implement additional monitoring on the API gateway to detect configuration errors and resource bottlenecks more quickly.
* **Incident Response Training:** Conduct regular training sessions for the engineering team to improve communication and collaboration during incident response situations.
