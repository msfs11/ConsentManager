# Intro
## Why?
- How to recognize if the user has signed all new versions of the consents?
- How to obtain evidence that the user gave consent in case of claims (from users, regulators and courts)?

## What is it?
ConsentManager is a microservice that manages user consents. It provides an API for managing user consents, stores and retrieves consent data in a database, and enforces consent policies. 

## For users:
- Control over their personal data: Consent management gives users control over their personal data by allowing them to choose what data they want to share with a company and how it can be used.
- Transparency: Consent management ensures that users are informed about how their data will be used and who will have access to it.

## For companies:
- Compliance with privacy regulations: Consent management helps companies comply with privacy regulations such as GDPR, CCPA, and others, which require companies to obtain explicit consent from users before collecting and processing their personal data.
- Avoidance of regulatory fines: Consent management helps companies avoid regulatory fines by ensuring that they collect and process data only with the appropriate consent.
Increased brand value and customer loyalty: With consent management at the core of the marketing strategy, companies can increase brand value and boost customer loyalty.
- Trust and transparency: Consent management helps companies build trust and transparency with their customers by being transparent about how their data will be used and who will have access to it.

# Glossary
- Consent: The agreement or permission expressed through affirmative, voluntary words or actions that are mutually understandable to all parties involved, to engage in a specific act at a specific time.
- Consent management: The process of systematically informing users about how a business collects and uses private data, and giving users the opportunity to provide (or deny) consent to this usage.
- GDPR: General Data Protection Regulation, a regulation in EU law on data protection and privacy for all individuals within the European Union (EU) and the European Economic Area (EEA).
- CCPA: California Consumer Privacy Act, a privacy law in California that enhances privacy rights and consumer protection for residents of California, United States.
- Data privacy: The protection of personal information or data from unauthorized access, use, disclosure, or destruction.
- Audit trail: A record of all the activities related to a particular operation or process, used to track and monitor the actions of users and systems.
- Personally Identifiable Information (PII): Any information that can be used to identify the PII Principal to whom the information relates to.
- PII Principal: The natural person to whom the personally identifiable information (PII) relates to.
- Purpose: The business, operational or regulatory requirement for the collection, use and/or disclosure of a PII Principal's data. In other words, it is the reason personal information is collected by the entity.
- Consent Receipt: A record of a consent interaction (or consent record summary linked to the record of consent) provided by a PII Principal to a PII Controller to collect, use and disclose the PII Principal’s PII in accordance to an agreed set of terms.
- PII Controller: A private stakeholder that determines the purposes and means for processing personally identifiable information (PII) other than the natural persons who use data for personal purposes.


# Scope and Limitations
Data storage:
the service doesn't store any personal data, it stores only uuid of the users from exteral systems.

Administration functions and interface, including user roles and permissions, user authentication, and access control, are not in the scope of this microservice. The microservice primarily focuses on providing consent management functionality for users and secure API routes for administering consents with token-based identification.

According to the twelve-factor methodology, the service is not providing any logging and metrics capabilities and writes its unbuffered event stream to stdout.


# Diagrams
## Container diagram
![Container diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/msfs11/ConsentManager/main/docs/container.puml)

## Component diagram
![Component diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/msfs11/ConsentManager/main/docs/component.puml)

## ER diagram
![ER diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/msfs11/ConsentManager/main/docs/er.puml)

## Use cases diagram
![Use cases diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/msfs11/ConsentManager/main/docs/usecase.puml)

### Onboarding
During the onboarding process, new users can sign a policy agreement and give their consent for data collection and processing. ConsentManager stores the consent data in the database and enforces the consent policies.

![Onboarding sequence diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/msfs11/ConsentManager/main/docs/sequence-onboarding.puml)

### Registered users
![Registered users sequence diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/msfs11/ConsentManager/main/docs/sequence-registered.puml)


### Administration
According to CRUD operations.

Administration allowed only by the provding Auth-token in headers.

**Create new consent**
```
POST /consents 
```

**Retrieve consent**
```
GET /consents/{uuid}
```

**Update consent**

```
PUT /consents/{uuid}
```

**Mark consent as not active**
```
PATCH /consents/{uuid}
Request body:
{
  active: true/false
}
```

### Compliance operations
**Get consents signed by user**


Policy updates: When a company updates their policy, existing users can be notified and asked to review and . ConsentManager updates the consent data in the database and enforces the updated consent policies.
Admin management: ConsentManager provides ability for monitoring received consents and data-subject requests. ConsentManager stores the consent data in the database and enforces the consent policies.


Consent and data sharing management: Consent Manager provides APIs for building consent pages and integrating them with an authorization platform. This flow enables businesses to give their customers the option to share their data with third-party providers in open finance ecosystems



## Deployment diagram
![Deployment diagram](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/msfs11/ConsentManager/main/docs/deployment.puml)

# Functional requirements
User Consent Management: ConsentManager should provide an API or user interface that allows users to give, withdraw, and manage their consent for data collection and processing activities.
Consent Data Storage: ConsentManager should store and retrieve consent data in a secure and reliable database. The system should be able to handle a large volume of consent records efficiently.
Consent Policy Enforcement: ConsentManager should enforce consent policies defined by the organization or mandated by privacy regulations. It should ensure that data collection and processing activities are performed only with explicit user consent.
Compliance with Privacy Regulations: ConsentManager should support compliance with privacy regulations such as GDPR, CCPA, and others. It should provide mechanisms to capture and document user consent in a manner that meets the requirements of these regulations.
Consent Tracking and Audit: ConsentManager should track and log user consent activities, including the date and time of consent given or withdrawn. This information should be easily accessible for auditing purposes.
User Data Management: ConsentManager should provide functionality to manage user data, including the ability to update, delete, or export user data upon request.
Regulatory Compliance Reporting: ConsentManager should generate reports and provide insights on consent management activities to support regulatory compliance efforts.
Integration Capabilities: ConsentManager should be able to integrate with other systems and applications within the organization's technology landscape, such as customer relationship management (CRM) systems or data analytics platforms.

# Non-functional requirements
## Legal cleaness
GDPR is a European Union law enacted on 25 May 2018 that requires companies to protect the data and privacy of all European residents. The seven key principles are:

Lawfulness, fairness, and transparency
Purpose limitation
Data minimization
Accuracy
Storage limitation
Integrity and confidentiality (security)
Accountability

### GDPR Requirements
GDPR itself contains several features each system must support:

Right to erasure (also known as Right to be Forgotten): If API stores the personal data for a user and the user requests for their data to be erased, API must erase the data.
Right to rectification: If API stores the personal data for a user and the user changes their data, API must either erase or update the data.
Right to be informed: You must inform users if you collect and use their personal data.


## Localizability
Internationalization Support: The system should be designed with internationalization in mind, following best practices and standards to ensure that it can be easily localized for different languages and regions. This includes using Unicode encoding, separating user interface text from code, and providing support for right-to-left languages, if applicable.
## Security
The ConsentManager microservice should implement appropriate security measures to protect sensitive user data and ensure compliance with privacy regulations.
For administrative functions public key encryption can be employed to secure the transmission and storage of consent data.

# Technical implementation
Programming Language: Python
Database: PostgreSQL
Web Framework: FastAPI
## API reference
https://editor.jsight.io/r/MBJeN6v/
