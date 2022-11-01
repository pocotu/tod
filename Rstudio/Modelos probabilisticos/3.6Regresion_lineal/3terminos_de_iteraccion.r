# It is easy to include interaction terms in a linear model using the lm() function.
# The syntax lstat:black tells R to include an interaction term between
# lstat and black. The syntax lstat*age simultaneously includes lstat, age,
# and the interaction term lstat×age as predictors; it is a shorthand for
# lstat+age+lstat:age.

summary(lm(medv ~ lstat * age, data = Boston))

