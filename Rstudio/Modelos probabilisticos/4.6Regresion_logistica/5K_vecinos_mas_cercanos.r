library (class)
train.X=cbind(Lag1, Lag2)[train,]
test.X=cbind(Lag1, Lag2)[!train,]
train.Direction = Direction[train]

set.seed(1)
knn.pred=knn(train.X, test.X, train.Direction, k=1)
table(knn.pred, Direction.2005)

(83+43)/252

knn.pred=knn(train.X, test.X, train.Direction, k=3)
table(knn.pred, Direction.2005)

mean(knn.pred == Direction.2005)
