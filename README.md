
### Python Terminal Application

#### By Jye Calder-Mason

Github: https://github.com/jyenese/terminalapp

# TRAVEL LOG

#### **Description (Brief overview)**
-  An easy reading application that you can add, view, edit or delete future or previous travel locations. 

-  A travel log for all of your previous travels where you can view the time you went, how many days you were there, additional comments about the trip, and how much you rated it.

- A leaderboard ranking system, which ranks the highest to lowest scored rating per travel on a seperate directory.

- Wishlist directory with a viewing board and add function.

#### **Functionality**

As starting the application you are prompted with a menu asking you for input from 1-8 (numeric) on which function you'd like to explore.
![menu](./resources/travel_menu.png)

### **Travel Directory**

  Once selecting "1" the 'Travel Directory' will show a a dictionary of previous travels. Starting with name, the date you visited, the duration of the travel in 'Days' and the score rating out of 10. (10 being best)

 ![travel_dict](./resources/travel_dict.png)

- To exit back to the menu, the option to click 'Enter' is available after every functional abilty.

### **Leaderboard**

Once selecting "2" the 'Leaderboard' will show your travel dictionary but from highest to lowest rating. (10 being at the top, 1 being at the bottom)

![leaderboard](./resources/leaderboard.png)

- As you can see its now viewing the same directory as the travel directory, but rating changes the way it lists.

### **Adding future/previous travels**

Once selecting "3" a prompt for user input will ask "What is the name of the location?" the user will need to type in a brief name of the location then hitting the 'Enter' button on the keyboard.
![add_name](./resources/test1.png)

After entering the name of your travel, user input will be prompted for a date to which you would like to travel or have travelled to this location.

![add_date](./resources/test2.png)

Once adding a date, user input will be prompted asking for the duration in 'days' format (5 days)etc.

![add_duration](./resources/test3.png)

Next step, user input needed for additional comments. Here you can add any comments for you to view at a later date about the trip. (How much it cost, what were the best parts, who you went with, what went wrong, etc)

![add_comment](./resources/test4.png)

And the last user input is the rating. After the additional comment, the application will prompt you for a rating from 10 to 1, 10 being the highest. The rank rating system is viewable via the leaderboard.

![add_rating](./resources/adding_func.png)

As shown its been added into the Travel Directory and the leaderboard!

![leaderboard_add](./resources/example_add.png)

### **Deleting**

After typing in "5" in the menu the application will prompt the user for a date of the destination. 

The Travel directory will be prompted for easy viewing of which travel you'll be deleting. For example Barcelona would be 7/8/2017

Its the date your deleting as its the only part of the item which is seperate from mutliples. If it was prompt for name of location(Good chance you could have been to the location twice, then making the display an annoyyance.)

![delete](./resources/example_delete.png)

Once deleting the application will accept the input and prompt with "has been removed" In this example I have removed 'This is a test, 1/11/11, 5 days, 10.0"

![delete_refresh](./resources/show_delete.png)


### **Editing**

Same as the delete function, as you type the "6" key, you'll be prompted with the travel directory to see which travel you'd like to edit. Same function of picking the date for the same reasons as above.

Once picking the date of which travel you'd like to edit, another prompt will ask for user input on what part of the item you'd like to edit. (Name, date, duration, rating).

To follow the example, I'm going to edit the rating. After typing in 'rating' another user input will prompt asking what you would like to change the rating too. After this the item will be updated into the directory.

![edit_example](./resources/example_edit.png)

As shown the time I went to Queenstown, the rating was changed from 8.5 to 8.6.

![menu](./resources/edit_example2.png)

### **Info Panel**

"7" function on the menu prompts the "More information panel" where you can view the travel in a more direct aspect and view the comments added.

The application will prompt you with the travel directory, for easy choosing of which to pick. As a theme you will be choosing the destination via the date.

User input asked for "What was the date from the travel log?"

Here are two examples of what will show up. One being a previous travel, the other being a new addition.

![info](./resources/info_panel1.png)
![new_info](./resources/info_panel2.png)

### **Wishlist**

The wishlish function is there to add future trips, to a seperate directory. This has got nothing connected with the Travel directory. Once you prompt the wishlist with the "7" key you are asked by the application for input on which you'd rather do;

- **view:** Shows all the items on your wishlist. The name, the date you'd like to travel, days potential, and how much its going to cost.

![menu](./resources/wishlist_view.png)

- **add:** prompts you for input. Starting off with the name of the destination you'd like to travel.
- After adding the destination, user input will be prompted again with the application asking for the date you'd like to travel to this location.
- After adding the date, another user input will be prompted asking for the duration, and then again with the cost.

- After hitting the 'Enter' key, the application will confirm the details and publish it into the Wishlist.

![menu](./resources/wishlist_add_example.png)

- After adding, it will appear in the wishlist view menu.

![menu](./resources/wishlist_updated.png)

### **Exit**

You know the drill, if you hit the 8 key, I have to send you my regards and thank you for using the travel log.

![menu](./resources/end.png)


## **Instructions to install Python**

**Prerequisites**

- A system running Windows 10 with admin privileges
- Command Prompt (comes with Windows by default)
- A Remote Desktop Connection app (use if you are installing Python on a remote Windows server)

Python download link: https://www.python.org/downloads/windows/
1. Pick which version you're going to download. Which is going to be Python3.

2. Download the python executable installer.

3. Run the installer.

4. Verify it was added via Command prompt with opening up command prompt and typing in
    > python --version
    
    After verifying, it should say which version is added to the computer.
5. All installed and ready to give the travel log a run!

### **Design Proccess**

Straight of the bat I knew what I was going to create, something that I loved to do before COVID. Traveling around the world, exploring new places, checking out different cultures etc.

After one of the classes I was brainstorming on a peice of paper what I'd like to be added into the log, what features I'd like to have, what I want it to look like, all the good stuff. 

![proccess](./resources/TRAVEL_info1.jpeg)

With this being so early on, I was so new to what potential features I could add in, or what ways to get into the different directories. 

After a few days of adding in the basics, customizing function and definitions, I went back to the drawing board to think of new ideas to add into the travel log. In came the 'More info panel' and the 'Wishlist'.

I didn't really use a flow chart to vibe my idea with so, it was more or less just how Id like the application to flow.

![process2](./resources/travel_info2.jpg)

![process2](./resources/checklist.png)

![process2](./resources/presentation/testing.png)
