#include "mainwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    // start instance of our window
    MainWindow w;
    w.show();

    return a.exec();
}
