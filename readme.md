# Fraud Detection in Insurance Claims
#### Help insurance companies identify which policies are fraudulent

## 1.Introduction
In the past, fraud detection was relegated to claims agents who had to rely on few facts and a large amount of intuition. New data analysis has introduced tools to make fraud review and detection possible in other areas such as underwriting, policy renewals, and in periodic checks that ﬁt right in with modelling. 

The role this data plays in today’s market varies by insurer as each weighs the cost of improving upon information systems versus the losses caused by current fraud. This often comes down the question of: <b>is fraud creating a poor enough customer experience that infrastructure investments will improve fraud detection and improve honest customer claims processes? </b>

Protection of personal information is paramount, but fraud pattern recogni¬tion requires a large amount of data from underwriting, claims, law enforce¬ment and even other insurers. Each new piece of legislation has only made the protection hurdle higher when integrating these sources. 

Fraud is a growing in every sector and in the insurance sector estimates billions of dollars to the industry. Machine learning algorithms can simply eliminate human errors and separate unobserved fraud patterns by identifying exceptions. Insurance companies rely on predictive models use the preceding cases of falsified actions.The machine learning algorithms with new data have much more perfect
fraud detections.

## 2. Problem Description
Given the dataset containing different parameters of insurance claims, data can be from different sources and ingestion pipelines but here we have a final combined datset from kaggle, build a Machine Learning Model that will predict whether a customer is placing a fraudent insurance claim or not.

## 3. Data Description
The data contains the following attributes/Features:

*   months_as_customer: It denotes the number of months for which the customer is associated with the insurance company.
*	age: continuous. It denotes the age of the person.
*	policy_number: The policy number.
*	policy_bind_date: Start date of the policy.
*	policy_state: The state where the policy is registered.
*	policy_csl-combined single limits. How much of the bodily injury will be covered from the total damage.
https://www.berkshireinsuranceservices.com/arecombinedsinglelimitsbetter  
*	policy_deductable: The amount paid out of pocket by the policy-holder before an insurance provider will pay any expenses.
*	policy_annual_premium: The yearly premium for the policy.
*	umbrella_limit: An umbrella insurance policy is extra liability insurance coverage that goes beyond the limits of the insured's homeowners, auto or watercraft insurance. It provides an additional layer of security to those who are at risk of being sued for damages to other people's property or injuries caused to others in an accident.
*	insured_zip: The zip code where the policy is registered.
*	insured_sex: It denotes the person's gender.
*	insured_education_level: The highest educational qualification of the policy-holder.
*	insured_occupation: The occupation of the policy-holder.
*	insured_hobbies: The hobbies of the policy-holder.
*	insured_relationship: Dependents on the policy-holder.
*	capital-gain: It denotes the monitory gains by the person.
*	capital-loss: It denotes the monitory loss by the person.
*	incident_date: The date when the incident happened.
*	incident_type: The type of the incident.
*	collision_type: The type of collision that took place.
*	incident_severity: The severity of the incident.
*	authorities_contacted: Which authority was contacted.
*	incident_state: The state in which the incident took place.
*	incident_city: The city in which the incident took place. 
*	incident_location: The street in which the incident took place.
*	incident_hour_of_the_day: The time of the day when the incident took place.
*	property_damage: If any property damage was done.
*	bodily_injuries: Number of bodily injuries.
*	Witnesses: Number of witnesses present.
*	police_report_available: Is the police report available.
*	total_claim_amount: Total amount claimed by the customer.
*	injury_claim: Amount claimed for injury
*	property_claim: Amount claimed for property damage.
*	vehicle_claim: Amount claimed for vehicle damage.
*	auto_make: The manufacturer of the vehicle
*	auto_model: The model of the vehicle. 
*	auto_year: The year of manufacture of the vehicle. 
*	fraud_reported:  Y or N

## 4. Perfomance Metric
AUC score





## References
https://www.reutersevents.com/insurance/fraud/role-data-and-analytics-insurance-fraud-detection
https://www.kaggle.com/c/fraud-detection-in-insurance-claims/overview