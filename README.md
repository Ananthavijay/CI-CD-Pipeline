### CI/CD pipeline of a FLASK CRUD API APP

- Piepline: Github -> Jenkins -> Sonar Qube -> Docker
- Jenkins fetches the source code from GitHub, performs a static analysis using SonarQube, then dockerizes the application, deploys it, and pushes the Docker image to Docker Hub so that others can get the latest image

#### Flask API:
1. Sign up:
<img width="679" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/81e83a08-5710-4023-8764-fdfe6b7a0ed3">


2. Sign in:
<img width="678" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/e454fd1f-62ad-4120-9608-6b1b35aa2899">

- Set the token as an environment variable so it can be used in subsequent requests in the Authorization header.

<img width="678" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/1a88c763-c3bf-46a4-a914-a44e64ed4492">

- The token in the environment variable can be referenced like this in subsequent requests

<img width="675" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/25b0b168-cb2b-4f37-9fcf-a8cd1a644a73">

3. Create Note

<img width="682" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/b262d804-3eaf-4bd4-a4ab-4b16efd5772e">

4. Update Note

<img width="682" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/31f4161b-8eaa-4adc-aed1-d9489ef0d4b5">

5. Get all notes that have been created

<img width="675" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/fa78e543-81db-4246-a0cd-99cf6721d88e">

6. Delete Note

<img width="680" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/3c40083c-8cc4-4d66-b30a-918c95bfaf00">

#### Docker:
- `Dockerfile` is used to build the Docker image

#### Jenkins:

- Pipeline script is the `Jenkinsfile`

<img width="627" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/6725b173-6369-4361-9c7e-1fbcd87e2c6b">

#### Sonarqube:
<img width="636" alt="image" src="https://github.com/Ananthavijay/CI-CD-pipeline/assets/35162705/06d0a008-11ae-4cad-9043-a6dc38543282">



