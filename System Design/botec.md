# Back Of The Envelope Calculations (B.O.T.E.C) Quiz

1. User Traffic Estimation:

   > Given a social networking site with 100 million active monthly users, if 10% of them are online concurrently and each generates 2 requests per minute, estimate the average requests per second the system must handle.

   ```
   Math:
   - 100,000,000 active monthly users
   - 10% online concurrently => 10,000,000 monthly concurrent users
   - Total requests per minute = 10,000,000 * 2 = 20,000,000
   - Total requests per second = 2,000,0000 / 60 = 1,000,000 / 3 ~ 333,333 requests per second

   Answer: 333,333K requests per second
   ```

2. Data Storage for Media:

   > A photo-sharing application allows users to upload images. Assuming 50 million users and an average of 1 photo per month per user with each photo being 2 MB, estimate the monthly and annual storage requirement.

   ```
   Math:
   - 50,000,000 users
   - 50M * 1 photo per month ~ 50,000,000 uploads per month
   - each photo = 2MB
   - 50M * 2MB = 100TB per month
   - Annual storage = 100TB * 12 = 1200TB ~ 2.4PB (petabytes)

   Answer:
   1. Monthly storage = 100TB
   2. Annual storage = 1.2PB
   ```

3. Bandwidth Calculation for Video Streaming:

   > Estimate the required bandwidth (in Gbps) if a video streaming service has 1 million concurrent viewers, each streaming video at 5 Mbps.

   ```
   Math:
   - 1,000,000 users
   - 5,000,000,000 bytes/second
   - Total required bandwidth: 5000 Gbps

   Answer:
   5000Gbps
   ```

4. Cache Sizing:

   > For a content-heavy website with 100 million page views per day, assume that 20% of pages are frequently accessed. How would you estimate the cache size (in number of pages) to effectively cover this hot data set?

   ```
   Math:
   - ASSUMPTION: total number of unique pages = 1M = 1,000,000
   - 20 % 1M = 200K

   Answer: 200K
   ```

5. Database Throughput:

   > If an online store experiences 500,000 transactions per day during peak season, with each transaction taking an average of 50 KB of data, calculate the daily data throughput and what read/write capacity you might need in your database.

   ```
   Math:
   - 500,000 transactions per day
   - 50KB data per transaction
   - 500,000 * 50,000 = 25,000,000,000 = 25GB per day

   Answer:
   25GB per day
   ```

6. API Rate Limiting:

   > You need to design an API rate limiter for an endpoint that sees 10,000 requests per second. How would you estimate the resources (CPU/memory) required to manage this traffic, considering each request takes roughly 5 ms to process?

7. Concurrent Connections:

   > A messaging platform expects 200,000 concurrent connections during peak hours. Estimate how many servers would be needed if each server can maintain 5,000 concurrent connections, including a safety margin of 20%.

8. Latency Impact Analysis:

   > Estimate the impact on user experience if the average network latency increases by 50 ms for a system that normally serves a page in 200 ms. How might this affect system design and capacity planning?

9. Server Cost Estimation:

   > For a microservices-based application with 10 services, each expected to handle 100 requests per second, estimate the number of servers needed if one server can handle 1,000 requests per second. Also, discuss how redundancy factors in.

10. Distributed Storage Estimate:

    > A distributed file storage system is required to store 1 petabyte of user data with a replication factor of 3. Calculate the total storage needed and consider the overhead of metadata.

11. Load Balancing Considerations:

    > If a load balancer distributes 50,000 requests per second across a fleet of servers, how would you determine the optimal number of backend servers, assuming each server can process 1,500 requests per second?

12. Backup and Disaster Recovery Planning:

    > Estimate the amount of backup storage needed if you must backup a 200 GB database daily and retain backups for 30 days, considering a compression ratio of 2:1 for the backups.

13. Queue Processing Capacity:

    > A task queue receives 100,000 jobs per hour. If each job takes approximately 0.1 seconds of CPU time, estimate the number of CPU cores needed to ensure jobs are processed in real time.

14. Network Infrastructure Sizing:

    > For a global application that serves 80% of its users in one region and 20% internationally, calculate the requirements for regional data centers if the local center can handle 90% of local requests and additional capacity is needed for international traffic.

15. Scaling for Sudden Traffic Spikes:

    > How would you estimate the additional capacity needed if your system must handle a sudden 3x spike in traffic during a flash sale event, given baseline usage numbers?

16. Caching Impact on DB Load:

    > Assuming that implementing a caching layer reduces database read load by 80%, estimate the new read query volume if the original load was 10,000 queries per second.

17. API Response Time Budgeting:

    > Design an API with an end-to-end response time of 300 ms. Break down the time allocation for network latency, server processing, and database access, and explain how you would plan capacity accordingly.

18. Estimating Log Data Ingestion:

    > A service generates 500 MB of log data per day per server. For a fleet of 200 servers, calculate the total daily log ingestion, and discuss how you’d plan storage and processing capacity for real-time analysis.

19. Microservices Intercommunication Overhead:

    > In a microservices architecture with 50 services, if each service makes 10 inter-service calls per request and you expect 1,000 requests per second, estimate the total number of internal calls per second and how that affects network throughput.

20. Capacity Planning for Batch Processing Jobs:
    > A system processes 10 TB of data daily using batch jobs. If the processing job runs over a 12-hour window, estimate the data processing rate (in MB/sec) required, and discuss potential strategies for horizontal scaling.
