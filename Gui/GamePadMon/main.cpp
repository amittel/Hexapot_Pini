#include "dialog.h"
#include <QApplication>
#include "gamepadmonitor.h"

int main(int argc, char *argv[])
{
        QApplication a(argc, argv);
        Dialog w;
        w.show();

        GamepadMonitor monitor;
        return a.exec();
}
