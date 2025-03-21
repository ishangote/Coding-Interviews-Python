# Perseverance

## Flashcard: Perseverance

**Situation:**

- Previous company's sales territory planning tool migrated to Salesforce.
- Data sync between Salesforce and AWS backend delayed (3-4 hours), impacting sales productivity.
- Issue persisted for 2 years; team accepted the status quo due to Salesforce API limitations.

**Task:**

- As Lead Backend Engineer, challenged myself to solve this persistent issue using Salesforce's new Platform Event service.
- Overcame leadership skepticism about scalability and reliability.

**Action:**

- Conducted deep research into similar solutions within Amazon teams.
- Built a proof-of-concept (POC) with AWS Event Buses and Lambda functions.
- Collaborated with Salesforce account team to increase Platform Event limits.
- Created detailed design documents, including cost-benefit analysis and expected outcomes.
- Mentored two junior engineers; implemented robust monitoring and reconciliation frameworks.

**Results:**

- Achieved 90% improvement, reducing sync time from 3-4 hours to under 5 minutes.
- Eliminated batch processing; system handled 100K+ territory updates daily without issues.
- Solution adopted company-wide by 5 other teams, becoming the AWS-Salesforce integration standard.
- Invited to present solution at SalesforceCon; received positive feedback internally and externally.
- Sales teams reported significant operational improvements; praised as transformative.

**Lessons Learned:**

- Persistence in the face of skepticism, thorough research, and structured problem-solving are key to impactful solutions.
- Refusing to accept the status quo can drive organizational change.

---

## Polished Sentences

1. "Despite the issue persisting for two years and multiple failed attempts to solve it due to Salesforce API constraints, most of the team had resigned themselves to accepting these delays as an unchangeable reality."
2. "When Salesforce released their Platform Event service in Winter '23, I saw an opportunity."
3. " I knew that if successful, this approach could become a template for other teams struggling with similar Salesforce integration challenges."
4. "To ensure buy-in, I created a comprehensive design document that included cost analysis, expected traffic patterns, and projected customer impact."
5. "Once approved, I led a small team of two junior engineers, mentoring them while implementing the solution."
6. "What started as a solution for our team quickly gained attention across the organization."

---

## Full Script

At my previous company, I was working on a critical sales territory planning tool that we'd migrated from our in-house system to Salesforce. We had a major pain point: data synchronization between Salesforce and our AWS backend was only happening twice daily through batch jobs. This meant our sales teams were regularly facing 3-4 hour delays in getting updated territory data, seriously impacting their ability to work effectively. Despite the issue persisting for two years and multiple failed attempts to solve it due to Salesforce API constraints, most of the team had resigned themselves to accepting these delays as an unchangeable reality.

As the lead backend engineer, I took on the challenge of finding a better solution. When Salesforce released their Platform Event service in Winter '23, I saw an opportunity. I proposed designing a real-time integration system using event-driven architecture, but faced significant skepticism from leadership about scalability and potential disruption to existing processes. My task was to not only architect and implement this solution but also to prove its reliability through extensive testing and documentation. I knew that if successful, this approach could become a template for other teams struggling with similar Salesforce integration challenges.

I began by thoroughly researching similar implementations across Amazon teams, learning from their successes and pitfalls. After identifying promising patterns, I built a proof-of-concept using AWS Event Buses and Lambda functions to demonstrate feasibility. When we hit Platform Event limitations, I didn't give up - instead, I built a detailed business case and worked with our Salesforce account team to secure increased limits. To ensure buy-in, I created a comprehensive design document that included cost analysis, expected traffic patterns, and projected customer impact. I then presented this alongside real customer feedback to build support among stakeholders. Once approved, I led a small team of two junior engineers, mentoring them while implementing the solution. I architected the service to be generic and reusable, anticipating similar needs across other teams. Throughout development, I implemented robust monitoring systems and data quality checks. Knowing data consistency was crucial, I also created a reconciliation framework to handle edge cases and ensure data integrity. Despite initial setbacks and skepticism, my persistence in refining the approach and addressing concerns systematically helped drive the project forward.

The results exceeded our expectations. We reduced data sync time from 3-4 hours to under 5 minutes - a 90% improvement that immediately impacted our sales teams' productivity. The event-driven architecture completely eliminated the need for batch processing, and the system proved robust during our busiest sales planning periods, handling over 100,000 territory updates per day without issues. What started as a solution for our team quickly gained attention across the organization. Five other teams adopted our framework, making it the standard for AWS-Salesforce integration company-wide. The success led to an invitation to present at SalesforceCon, where other companies expressed interest in implementing similar solutions. Most importantly, our sales teams reported significant improvements in their daily operations, with one sales director noting that it 'transformed how we handle territory planning.' Looking back, this project taught me that persistence in the face of skepticism, combined with thorough research and systematic problem-solving, can lead to solutions that benefit not just immediate stakeholders but the broader organization. The framework we built continues to serve as a foundation for new integration projects, proving that sometimes the most impactful solutions come from refusing to accept the status quo.
