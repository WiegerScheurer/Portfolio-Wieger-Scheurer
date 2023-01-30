main.style("body-background-color","#2f4f4f");
main.style("background-color","#2f4f4f");
main.style("color", "#ffefd5");
main.style("font-size","85%");
//Create background and define visual characteristics of the experiment.
text("Posner Task");
await(3000);
select("Please provide your gender",['male','female','other'],"gender");
input("What is your age?","age",3);
//Collecting demographics by using the select and input functions.
var main = new Box("#ffefd5", "#2f4f4f", "black", 100, 10, "r#8b0000", 1);
    d = main.addblock("center", 80, 100, 10, "#ffefd5"), //Button to navigate throught the experiment.
    all_trials = Array.from({ length: 100 }, () => Math.floor(Math.random() * 4)),
    t1 = 0,
    t2 = 0,
    RT = 0,
    RT_sum = 0,
    RT_avg = 0;
//Creation of an improved cosmetic environment and of some of the variables needed apart from the ones included in functions.
function intro_blocks() { //Introduction in a function to make the chronological calling later on more clear.
    txt = main.addblock(10, 10, 80, 25, "#ffefd5", "Welcome.");
    d.button("Continue", "intro_button", "continued", "knop")
        .style("background-color", "#f5deb3", "#knop")
        .await('click');

    txt.text("Be aware that you are able to quit this experiment at any given time. It is highly recommended, but not obligatory to complete the experiment once started.");
    d.button("I am aware of this", "intro_button", "continued", "knop")
        .style("background-color", "#f5deb3", "#knop")
        .await('click');
    
    txt.text("You'll be presented a fixation point in the middle of the screen with two similar boxes alongside it. Try to maintain a steady focus on this fixation point in the centre.");
    d.button("Understood", "intro_button", "continued", "knop")
        .style("background-color", "#f5deb3", "#knop")
        .await('click');

    txt.text("Press the Z button on your keyboard when you perceive a GO-signal in the left box, and the M button when you see that signal in the right box. Ignore any x-symbol appearing in either box.");
    d.button("Understood", "intro_button", "continued", "knop")
        .style("background-color", "#f5deb3", "#knop")
        .await('click');

    txt.text("Before starting there are 10 practice trials to make sure the experiment is understood.");
    d.button("Let's practice", "intro_button", "continued", "knop")
        .style("background-color", "#f5deb3", "#knop")
        .await('click');
    d.destroy();
    txt.destroy();
//Sequence of informative introductory text combined with buttons to manoeuvre through the boxes.
}
//Main function starting with the creation of the stimuli blocks and fixation point.
function trial_blocks(main, scenario) {
    var a = main.addblock(10, "center", 10, 10, "white", ""),
        b = main.addblock("center", "center", 10, 10, "#ffefd5", "+"),
        c = main.addblock(80, "center", 10, 10, "white", "");
//Combination of if and else if statements responsible for the creation of the different types of trials.
//Different scenario's represent different combinations of cue and GO-signal locations.
    var block_to_cue, block_to_go;
    if (scenario == 0) {
        block_to_cue = a;
        block_to_go = a;
        same_block = 1;
        correct_key = "z";
    } else if (scenario == 1) {
        block_to_cue = a;
        block_to_go = c;
        same_block = 0;
        correct_key = "m";
    } else if (scenario == 2) {
        block_to_cue = c;
        block_to_go = c;
        same_block = 1;
        correct_key = "m";
    } else if (scenario == 3) {
        block_to_cue = c;
        block_to_go = a;
        same_block = 0;
        correct_key = "z";
    }
await(500 + random(500));
    if (Math.random() < 0.6667){ // 66,67% chance a cue is given. Every type of trial has about 1/3 chance to occur, no cue, matching cue or mismatch cue.
        block_to_cue.text("x");
        logtrial(1, "cue_given");
    } else {
        logtrial(0, "cue_given");
    }
    await(100);
//The appearance of the GO signal, followed by timing of the response and disappearance of the created boxes.
    block_to_cue.text("");
    await(500 + random(500));
    block_to_go.text("GO");
    t1 = now();
    key_resp = awaitkey("z,m");
    t2 = now();
    RT = t2 - t1;
    a.destroy();
    b.destroy();
    c.destroy();
//Multiple logtrials to be able to categorize the collected response data during analysis.
    logtrial(same_block, "same_block");
    if (key_resp.key === correct_key) {
        logtrial(1, "correct_key_pressed");
    } else {
        logtrial(0, "correct_key_pressed");
    }
    logtrial(RT, "RT");
    // one log line: [cue_given, same_block, correct_key_pressed, RT]
}
//Calling of the previously created functions. Starting with the intro blocks.
intro_blocks();
await(2500);
//For loop with 10 set iterations in order to execute the practice trial set. Including the calculation of average response time.
for (var i = 0; i < 10; i++) {
    trial_blocks(main, all_trials[i]);
    logtrial(1, "practice_trial"); //Discerning between trial and non trial response times by logging an extra binary variable. 
    RT_sum = RT_sum + RT;
    RT_avg = RT_sum / i;
    RT_avg = RT_avg.toFixed(2);
}
//Short introductory text and button for the definitive task.
txt = main.addblock(10, 10, 80, 25, "#ffefd5", "This was merely the practice round. Your average response time was: " + RT_avg + "ms. Make sure you are mentally prepared for the real task.");
d = main.addblock("center", 80, 100, 10, "#ffefd5");
d.button("Let's begin", "intro_button", "continued", "knop")
    .style("background-color", "#f5deb3", "#knop")
    .await('click');
d.destroy();
txt.destroy();
//Reset of the calculated response time sum and average to make sure the data from the practice trial and the real task do not overlap.
RT_sum = 0;
RT_avg = 0;
//Once again a for loop including the grand function of the trials, this time with as much iterations as there are randomized stimuli combinations.
for (var i = 0; i < all_trials.length; i++) {
    trial_blocks(main, all_trials[i]);
    logtrial(0, "practice_trial");
    RT_sum = RT_sum + RT;
    RT_avg = RT_sum / i;
    RT_avg = RT_avg.toFixed(2);
}
//Concluding remarks, also mentioning the calculated response time average based on the collected data.
txt = main.addblock(10, 10, 80, 25, "#ffefd5","You've reached the end of the task. Your definite response time was: " + RT_avg + "ms. Thank you for participating!");
d = main.addblock("center", 80, 100, 10, "#ffefd5");
d.button("Ajeto", "intro_button", "continued", "knop")
    .style("background-color", "#f5deb3", "#knop")
    .await('click');
d.destroy();
txt.destroy();