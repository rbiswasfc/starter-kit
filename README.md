# starter-kit


# Introduction to machine learning in production (Coursera)

The machine learning code is actually 5-10% of the entire project code base. After building the Proof of Concept (PoC) in Jupyter Lab, a lot of of systematic steps needs to be completed to achieve a proper deployment (PoC to Production Gap). The entire ML project lifecycle needs a framework to organize tasks and provide ourself a structure to put things into perspective. The framework helps up to plan out all the important things that need to completed. The ML project lifecycle can be grouped into four basic steps:

1. Scoping
2. Data 
3. Modelling
4. Deployment

Let's explore the possible lifecycle of a machine learning project - Recommender System for Tourist Destinations

### Scoping
* Decide to work on a project
    * Build a recommender system for tourist attractions/destinations
* Decide on key metrics 
    * MRR or mAP
* Estimate resources and timeline

### Data
* Define data
    * How to get data?
        * Web scraping
        * Twitter, reddit, facebook, instagram api
    * Is the data labelled consistently?
        * Explore sequence of places visited by users

### Modelling
* What modelling to use?
    * Collaborative filtering
    * Content based filtering
    * Graph based leaning e.g Deepwalk

### Deployment
* How will the model be deployed?
* How to continuously monitor model performance?


Let's now deepdive into each of these steps.


### Deployment

#### Challenges
* ML Challenges
    * Data Drift
        * Gradual shift in data
        * Sudden shift in data e.g. during covid customer credit card behaviour changed posing challenges to fraud detection
        * User data generally has slower drift
        * Enterprise data (B2B application) can shift fast
    * Concept Drift
        * Change in X -> Y mapping e.g. increase in housing prices even though input features remain same
* Software Engineering issues
    * Realtime vs batch
    * Cloud vs edge/browser computation
    * Compute resources
        * CPU/GPU requirements
    * Latency and throughput (Queries per second - QPS)
    * Logging
    * Security and privacy

#### Deployment Patterns
Three types of use-cases during deployment
* New product/capability
* Automate/assist with manual task
    * Shadow mode deployment: ML system shadows the human and runs in parallel. ML systems output not used for any decisions during this phase. Gather data to assess effectiveness of ML model without replacing existing processes
    * When we are ready to use ML model, we can adopt canary deployment pattern. Roll out ML model to small fraction of the traffic initially and allow the model to make actual decision for this fraction of events. Monitor the system and gradually ramp up.
* Replace previous ML system 
    * Use a router to divide the traffic to blue (old) and green (new) version of the app. Snip up the new version of the app and distribute the traffic. If the new model does not perform as per expectation, then rollback.

Key aspects during deployment
* Gradual ramp-up with monitoring
* Rollback

Degrees of automation
* Human only
* Shadow mode
* AI assisted
* Partial automation
* Full automation

#### Monitoring
* Build a dashboard to monitor key metrics of the ML system. Common key metrics are:
    * Software metrics
        * Memory
        * Compute time
        * Latency
        * Throughput
        * Server load
    * Input metrics
        * Average input length (e.g. sound clip duration, text length)
        * Average input volume
        * Feature missing fraction
        * Image brightness
    * Output metrics
        * Null output percentage
        * Number of times user repeats the query
* Brainstorm how things could go wrong
* Brainstorm a few metrics that can detect the issues
* Use many tracking metrics to begin with and gradually remove the ones those are not helpful
* Monitoring machine learning pipeline
    * Complex cascading effects
    * Build metrics to monitor individual components of the pipeline

Deployment is iterative process:
Monitoring dashboard | Traffic | Performance Analysis


#### Notes
* Majority of companies reporting between 8 and 90 days to deploy a single model
* A significant portion of attempted deployments fail, due to lack of expertise, bias in data and high costs






* Scoping
    * Define project
* Data
    * Define data
    * Acquire data
    * Labelling
    * Baseline
* Modelling
    * Select and train model
    * Error analysis and back-testing
    * Perform audit to assess reliability 
* Deployment
    * Deploy in production
    * Monitor and maintain system
    * Concept drift or data drift