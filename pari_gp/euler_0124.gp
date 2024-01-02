radical(x)=F=factor(x)[,1];prod(i=1,length(F),F[i])
allocatemem(32000000)
vecsort(vector(100000, n, [radical(n),n]),1)[10000][2]
