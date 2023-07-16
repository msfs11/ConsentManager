# Initial Architecture Decision Record (ADR) - ConsentManager Microservice
# Architecture Decision Record (ADR) - ConsentManager Microservice

## Context
The ConsentManager microservice is responsible for managing user consents within the system. It handles the creation, retrieval, modification, and storage of consent-related data. To ensure proper organization and maintainability, it is important to define the architecture and design decisions for the ConsentManager microservice.

## Decision
To manage the history of administration actions on consents in the database, the following decisions have been made:

1. Create a separate table named "consent_admin_log" to store the log of administration actions on consents.

2. The "consent_admin_log" table will have the following columns:
   - `log_id`: A unique identifier for each log entry.
   - `admin_id`: The identifier of the administrator who performed the action.
   - `consent_id`: The identifier of the consent associated with the action.
   - `action_type`: The type of action performed on the consent (e.g., sign, revoke).
   - `timestamp`: The date and time when the action was performed.

3. Additional optional columns can be included based on specific requirements, such as `ip_address` to store the IP address of the administrator performing the action or any other relevant metadata.

## Consequences
By implementing the "consent_admin_log" table, the ConsentManager microservice gains the following benefits:

- A clear and organized log of administration actions on consents is maintained, providing an audit trail for compliance and accountability purposes.
- The history of consent-related actions can be easily retrieved and analyzed for reporting and auditing purposes.
- The log allows for tracking and monitoring of administrator activities, ensuring transparency and accountability within the system.

However, it is important to consider the potential impact on database performance and storage requirements due to the increased data volume in the consent administration log table. Proper indexing and optimization techniques should be applied to mitigate any performance concerns.
