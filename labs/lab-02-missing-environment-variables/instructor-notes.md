# Instructor Notes

## Teaching goal

Show learners that configuration bugs are often caused by load order, file location, or missing setup instructions.

## Discussion prompts

- Why should API keys not be hardcoded?
- What files should never be committed to Github?
- How can a README prevent this bug?

## Common learner mistake

Learners may recreate the `.env` file repeatedly instead of checking whether the app loads it before reading values.

## Production connection

Missing environment variables are common in deployments when secrets are not configured in the hosting platform.
