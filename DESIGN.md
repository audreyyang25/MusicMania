# Design
Our website has three primary components: the informational section, the multiple-choice quizzes, and the games.


(1) Informational section:
For this portion, we decided to have our homepage also display the overview of music history. We then embedded links to biographies of famous composers of each musical period, which would redirect the user to a new page.
In each of the composer bios, we embedded videos of famous compositions by those composers; we decided to make the video embedded rather than use links to redirect to a new page, because this would be easier for the user to access. For each of these pages, we extended the basic "layout.html" file and tailored it to our needs.  Some of the biographical information was obtained with the help of ChatGPT.


(2) Multiple-choice quizzes:
We designed the multiple-choice quizzes to essentially follow a point system. Using  javascript, we chose four categories for the user to be "placed in." Then, based on their answers, points would be added to the corresponding category. Ultimately, whichever category contained the most points would be the category that the user received as a result.
In terms of code, we decided to use radio buttons to give the user the option of only selecting one answer per question. Then, we used event listeners in javascript to carry out the point addition.
The point addition occurs at the very end, once the user presses submit, so that they can change their answers before then without impacting their results.
We decided to display the results on the same page as the quiz so that the user could immediately retake the quiz if they wanted to. However, we also decided not to reset points in between quizzes if they did not reload the page, because we felt that, given that these are essentially personality quizzes,
it is important to include all of their answers, especially those that they chose initially to submit.
Once again, we extended the "layout.html" file to create these webpages.


(3) Games:
We designed the games by embedding audio files into the webpage. Then, we decided to allow free-response for the perfect pitch quiz to make it slightly more difficult and really test if the user can identify the pitch.
In addition, we decided to make the perfect pitch quiz all or nothing, because missing one question would mean that the user does not have perfect pitch.
We did a similar implementation for the composer identification game by embedding audio files and allowing free response answers. This time, we just assign point scores based on correct answers.


In addition, we have the composers tab.
(4) Composers:
We designed the composers page by finding images of composers and putting them into a table. Then, we linked the pages of each of the composers to their images. We decided to sort the composers by period via the columns. We wanted the columns to all be of the same width and the number of columns to change depending on the screen size. This would make the image easy to see on all devices. For the image grid, starter code was adapted from https://www.w3schools.com/howto/howto_css_image_grid_responsive.asp.
