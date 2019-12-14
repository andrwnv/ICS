#ifndef INDUSTRIALCONTROLSYSTEM_H
#define INDUSTRIALCONTROLSYSTEM_H

#include <QMainWindow>

class IndustrialControlSystem : public QMainWindow
{
    Q_OBJECT

public:
    IndustrialControlSystem(QWidget *parent = nullptr);
    ~IndustrialControlSystem();
};
#endif // INDUSTRIALCONTROLSYSTEM_H
