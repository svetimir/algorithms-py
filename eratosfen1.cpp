/*
    Решето Эратосфена
    Пример реализации на C++
    03.02.2015
    flaurion.livejournal.com
*/

/*
    USAGE:
    eratosfen_flxd.exe -n <NUM>
    NUM - maximal number

    (c)2015 Georgy Yashin, ifi@yandex.ru
*/

#include <vector>
#include <cstdio>
#include <cstring>

using namespace std;

void usage()
{
    printf("eratosfen_flxd.exe - search and print all simple numbers lesser than given\nUSAGE:\neratosfen.exe -n <NUM>\nNUM - maximal number\n(c)2015, Georgy Yashin, ifi@yandex.ru");
}

int main(int argc,char*argv[])
{
    int i=0,n;
    /*
        Обработка параметров
    */
    if(argc<3)
    {
        usage();
        return 0;
    }
    for(i=0;i<argc;i++)
    {
        if(strcmp(argv[i],"-n")==0)
        {
            sscanf(argv[i+1],"%d",&n);
        }
    }
    /*
        Изначально заполняем массив истинными значениями
    */
    vector<bool>table(n);
    for(i=0;i<n;i++)
    {
        table[i]=true;
    }
    int t=2;
    /*
        Главная часть алгоритма
    */
    while(t<n)
    {
        /*
            Просеиваем числа
        */
        for(i=2*t;i<n;i+=t)
        {
            table[i]=false;
        }
        /*
            Находим следующее простое число в массиве,
            большее чем t, и присваиваем t
        */
        t++;
        while(!table[t])
        {
            t++;
        }
    }
    printf("Simple numbers up to %d found\n",n);
    int s=0;
    for(i=0;i<table.size();i++)
    {
        s=(table[i]?i:0);
        if(s==0) continue;
        printf("%d ",s);
    }
    return 0;
}
