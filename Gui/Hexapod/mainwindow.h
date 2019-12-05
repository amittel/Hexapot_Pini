#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actionBeenden_triggered();

    void on_actionHexapod_Einrichtung_triggered();

    void on_actionInfo_triggered();

    void on_arrow_left_Button_clicked();

    void on_arrow_left_up_Button_clicked();

    void on_arrow_up_Button_clicked();

    void on_arrow_right_up_Button_clicked();

    void on_arrow_right_Button_clicked();

    void on_arrow_down_Button_clicked();

    void on_dial_valueChanged(int value);

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
