# Conflict Resolution

## Flashcard: Conflict Resolution

**Situation:**

- Across our sales planning services, we lacked a centralized data service.
- Teams independently built integrations to access data from one another on an ad-hoc basis.
- This approach significantly increased workload and resulted in unvalidated, inconsistent data across services.
- Sales teams frequently faced discrepancies, particularly affecting territory management and compensation calculations.

**Task:**

- Standardize data handling across services to create a single source of truth.
- Address resistance from two sister teams invested in their own integration solutions.

**Action:**

- Conducted methodical, empathetic discussions to understand resistance from sister teams.
- Organized technical meetings and presented data-driven evidence showing impacts of fragmented systems.
- Proposed a phased implementation approach to address concerns and incorporate existing solutions.
- Actively collaborated with resistant teams to integrate their solutions gradually.

**Results:**

- Achieved an 80% reduction in data discrepancies within six months.
- Restored sales teams’ trust with consistent data for territory management and compensation.
- Created a collaborative, successful model for resolving technical conflicts across organizational boundaries.
- Recognized internally as a best practice for managing technical change, leading to mentorship opportunities.

**Lessons Learned:**

- Effective conflict resolution requires empathy, active listening, and collaborative problem-solving.
- Technical excellence combined with interpersonal understanding transforms resistance into support.

---

## Polished Sentences:

1. "The lack of a single source of truth wasn't just a minor issue—it significantly impacted our entire sales operations process."
2. "My challenge wasn't just technical—I needed to standardize data handling while acknowledging the valuable work other teams had already done."
3. "Through patient negotiation and gradual implementation, I successfully turned initial resistance into enthusiastic adoption."
4. "This experience reinforced my belief that technical solutions are only effective when we build consensus and trust among stakeholders."

---

## Full Script

While working as a software engineer at AWS Sales Operations, I encountered a significant challenge during our annual planning cycles. Across our sales planning services, we lacked a centralized data service. This absence meant teams independently built integrations to access each other's data on an ad-hoc basis. Not only did this approach significantly increase workloads and complexity, but it also led to inconsistent and unvalidated data flowing between services. As a result, our sales team frequently reported serious discrepancies, especially regarding territory management and compensation calculations. These inconsistencies weren't just minor inconveniences; they caused cascading data issues throughout our sales operations, undermining the accuracy and reliability of critical business decisions.

As the senior engineer on the team, my manager tasked me with leading the effort to resolve these data inconsistencies. I needed to design a unified data synchronization system that would serve as the single source of truth across all services. However, I quickly discovered that two sister teams had already invested significant resources in their own integration solutions and were resistant to change. My challenge wasn't just technical – I had to find a way to standardize our data handling while acknowledging and incorporating the valuable work these teams had already done.

I took a methodical approach to address both the technical and interpersonal challenges. First, I created a comprehensive design document outlining a centralized data service architecture, incorporating a Pub/Sub mechanism and Server Sent Events for real-time data synchronization. However, before presenting this solution, I initiated one-on-one conversations with the leads of both resistant teams to truly understand their concerns and investment in their existing solutions. These discussions revealed specific pain points and technical constraints I hadn't initially considered. Armed with this insight, I organized a series of technical discussions where I presented data-driven evidence of how our fragmented approach was impacting business operations. Instead of pushing for an immediate complete transition, I proposed a phased onboarding strategy that would allow teams to gradually migrate while maintaining their current integrations. I personally committed to supporting each team through the transition, offering to help with integration code and providing detailed documentation. Through several weeks of patient negotiation, I demonstrated how the new system could coexist with and eventually enhance their existing solutions. This approach helped build trust and ultimately secured buy-in from both teams.

The results of this collaborative approach exceeded our expectations. Within six months of implementing the new system, we achieved an 80% reduction in data discrepancies across our services. This dramatic improvement restored our sales team's confidence in our systems, as they could now rely on consistent territory and compensation data. The unified data platform significantly streamlined decision-making processes, enabling leadership to make faster, more informed choices based on reliable data. Beyond the immediate benefits, we established a scalable foundation that made it easier for other teams to integrate their services. Perhaps most importantly, this experience created a successful blueprint for handling cross-team technical conflicts. By prioritizing understanding, demonstrating empathy, and focusing on gradual implementation, we turned initial resistance into enthusiastic adoption. The project's success led to its recognition as a model approach for driving technical change across organizational boundaries, and I now regularly mentor other teams facing similar challenges. Looking back, this experience reinforced my belief that technical solutions are only as effective as our ability to build consensus and trust among stakeholders.
