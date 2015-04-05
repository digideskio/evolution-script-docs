# evolution-script-docs
Documents for Evolution Script. https://scratch.mit.edu/projects/55653930/

Let's start with variables:

Variables are made with (and changed with) "=":
x=3
x="derp"
(x is the variable, "derp"/3 is the value.)

Task: Create a variable called "derp" with a value of "Hi!"

Alright, that's all good, but what about recalling the variable?

You can use the variable name to recall the variable.

x
(returns "derp"/3)

Task: Recall your derp variable.

Great, but can I find if the value of x is something?

Yep! You use "==" to compare.

x==3
x=="derp"
(x is being compared to "derp"/3 and returns true/false)

Huh... What about if it is NOT something?

x!=3
x!="derp"
(checks if x is NOT something)

Ok, ok! Fine...

Task: Compare derp to something

Hmm... What if I want to find the variable type?

Well, so far, you can use .(an identifier)?

x.str?
x.bool?
x.num?
x.int?
x.float?
(they return true or false)

Task: Compare derp to a boolean (.bool?)

Nice, but programming languages have got to have lists... Hopefully yours doesn't start on 0...

No, it doesn't! You don't even need square brackets! They are called "arrays" by the way...

x="Hi!", "Hello!", 3, 4.3, 55, 90, "Thing!"
x[4]
(x is given items, x[4] returns 4.3 as it is the fourth item)

Task: Make derp into an array of at least 3 items and return one of the items.

Issues:

Thanks for going through the tutorial! You may have noted some things it doesn't have.

x=y is not currently possible.
x[y] is not possible.
Where are all the other comparing operators?

Soon to come! (maybe)


