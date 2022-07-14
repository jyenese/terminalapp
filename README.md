
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
