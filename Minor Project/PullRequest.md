<h1> Step-by-Step Guide: Submitting Your Minor Project for Evaluation via Pull Request </h1>

## Introduction:
Welcome to our step-by-step guide on submitting your minor project for evaluation through a pull request! 

As a student, you've invested time and effort into developing an impressive project, and now it's time to showcase your skills and submit it for evaluation. In this tutorial, we will walk you through the process of forking the repository, making the necessary modifications for your project, and opening a pull request to submit it for evaluation. 

By following these steps, you'll have the opportunity to present your project to our team and receive valuable feedback. Let's get started and make your submission process smooth and successful!

## Step 1: Fork the Repository
Fork our repository to create your own copy. 

Go to our project repository [AIMLMonth2023](https://github.com/aiclub-igdtuw/AIMLMonth2023) on GitHub and click on the "Fork" button at the top-right corner of the page. This will create a personal copy of the repository under your own account.

## Step 2: Clone the Forked Repository
Once you have forked the repository, it's time to clone it to your local machine. Open your preferred terminal, command prompt or Git Bash and use the following command:
```
git clone https://github.com/<Your GitHub Username>/AIMLMonth2023
```
Don't forget to put your GitHub username in place of < Your GitHub Username >

```
cd AIMLMonth2023
```

## Step 3: Create a New Branch
To keep your changes separate from the main repository, let's create a new branch. Use the following command:
```
git checkout -b minorproject
```

## Step 4: Make Your Changes
Fill the details asked in ProjectSubmission.md file. You can use any text editor like VS Code to do so.

## Step 5: Commit and Push Your Changes
Once you are satisfied with your changes, it's important to commit and push them to your forked repository. Follow these steps:

Use the command `git add .` to stage all the modified files.
```
git add .
```

Next, commit the changes with a descriptive message using the command:
```
git commit -m "<Your Roll no - Your Problem Statement Title>"
```
Don't forget to add your roll no and Problem Statement Title in place of < Your Roll no - Your Problem Statement Title >

Finally, push the changes to your forked repository with the command:
```
git push origin minorproject
```

## Step 6: Open a Pull Request
Now that you have committed your changes to your forked repository's minorproject branch, it's time to submit it as a pull request to us for review.

* Ensure you are on the "minorproject" branch in your GitHub repository.

* On the repository page, you will see a message indicating that you are one commit ahead of the main branch.

* Look for the "Contribute" button (or a similar option) and click on it.

* From the dropdown menu, select "Open pull request."

* Make a pull request with < Your Roll no - Your Problem Statement Title > as the pull request title.

* Optionally, write a brief description elaborating on the modifications you made or any additional information you would like to share.

* Review the changes and files that are being included in the pull request.

* Double-check that the "base" branch is set to the main branch.

* When you're ready, click on the "Create pull request" button to submit your pull request.
