#include "IndustrialControlSystem.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    IndustrialControlSystem ui;
    ui.show();
    return a.exec();
}
