# my-cookbook

## Links:

[Team Spreedsheet](https://docs.google.com/spreadsheets/d/1hKtgQ5t0tkRawq-LUhJB8PN4NPBmyvGZ9104j4OYsQo/edit?usp=sharing)

[Git Links](https://docs.google.com/document/d/1Rm4ZFx0NWglbLO_My3vsZ5UCj4ztsCsujRUsgrwh-kU/edit?usp=sharing)

[Upstream Branch](https://www.geeksforgeeks.org/how-to-set-upstream-branch-on-git/?fbclid=IwAR0PjfBpXNjg3K_D7IT08zvWw8_NOCrEwjn_TthBTHSYhwMyWatcxDCUgV8#)

## Recommended Setup (WORK IN PROGRESS):

I recommend downloading [VS Code](https://code.visualstudio.com/) an installing the [MongoDB VS Code extension](https://marketplace.visualstudio.com/items?itemName=mongodb.mongodb-vscode). You need to also download [MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/).

## How to make changes:

1. Assign a ticket from Issues to yourself.

2. Enter the issue and click on `Create a branch` underneath Development in the sidbar. Try to name the branch according to what what you're actually doing. For example, if you want to edit the recipe filtering algorithm, you should name the branch something along the line of "edit-recipe-filter". Then checkout the branch locally. This is preferred so the branch is automatically linked with the issue Alternatively, you could create a new branch using `git checkout -b {your branch name here}`.

3. Make the necessary changes and test that they work locally.

4. One you've implemented the changes push you changes remotely and create a pull request.
   Pull requests should discuss the background of why it was necessary, the changes you made to the files and generally how they work, and how you tested the changes as well as pictures of the final result.

5. This repo is set so that other contributors have to comment on your pull requests in order for them to be able to be merged. Take their opinions into account and update your code accoringly!

6. Once the pull request has enough approvals, you can merge the pull request using Squash and Merge.

# Pull Request Formatting

Please use the following format when submitting pull requests:

### **Background:**

Give a background on why this change is necessary and why you chose to make the change.

### **Changes:**

Give a general overview of which files you changed and what changes you made to them.

Go into more detail about what changes were made to every file. Also talk about any assumptions you made while making the changes.
