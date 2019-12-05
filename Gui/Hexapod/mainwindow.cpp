#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <QDebug>
#include "settingsdialog.h"
#include "infodialog.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    // Set the Window Icon
    setWindowIcon(QIcon(":/data/files/Decepticons-Logo.png"));

    // Signal Slot part: SIGNAL from "Slider" to SLOT "Progressbar"
    //    connect(ui->horizontalSlider,SIGNAL(valueChanged(int)),
    //            ui->progressBar,SLOT(setValue(int)));



    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_actionBeenden_triggered()
{
    // Question
    QMessageBox::StandardButton reply;
    reply = QMessageBox::warning(this,"Bitte bestätigen Sie","Wollen Sie das Programm wirklich beenden?",QMessageBox::Yes | QMessageBox::No);

    if(reply == QMessageBox::Yes)
    {
        // Check for running connection to robot. If a connection is established,
        // prompt the user for confirmation to close programm.
        QMessageBox::information(this,"Information","Das Programm wird beendet.");
        // if yes, close app
        close();

    }
    else
    {
        QMessageBox::information(this,"Information","Das Programm wird fortgesetzt.");
        // if no, close dialog and go back to main window
    }
}

void MainWindow::on_actionHexapod_Einrichtung_triggered()
{
    // Opening this dialog will block userinput to the mainwindow ("setModal -> false")
    SettingsDialog sDialog;
    sDialog.setModal(false);
    sDialog.exec();
}

void MainWindow::on_actionInfo_triggered()
{
    // Opening this dialog will block userinput to the mainwindow ("setModal -> false")
    InfoDialog iDialog;
    iDialog.setModal(false);
    iDialog.exec();
}

void MainWindow::on_arrow_left_Button_clicked()
{
    // Change value from QDial
    ui->dial->setValue(90);
}

void MainWindow::on_arrow_left_up_Button_clicked()
{
    // Change value from QDial
    ui->dial->setValue(135);
}

void MainWindow::on_arrow_up_Button_clicked()
{
    // Change value from QDial
    ui->dial->setValue(180);
}

void MainWindow::on_arrow_right_up_Button_clicked()
{
    // Change value from QDial
    ui->dial->setValue(225);
}

void MainWindow::on_arrow_right_Button_clicked()
{
    // Change value from QDial
    ui->dial->setValue(270);
}

void MainWindow::on_arrow_down_Button_clicked()
{
    // Change value from QDial
    ui->dial->setValue(360);
}

void MainWindow::on_dial_valueChanged(int value)
{
    // for debugging purposes only
    qDebug() << value;
}
