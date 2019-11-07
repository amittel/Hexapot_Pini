#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include "settingsdialog.h"
#include "infodialog.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    // Set the Window Icon
    setWindowIcon(QIcon(":/data/files/Decepticons-Logo.png"));


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
    // The commented code runs, but keeps focus on opened window "MyDialog"
//    MyDialog mDialog;
//    mDialog.setModal(false);
//    mDialog.exec();
    SettingsDialog sDialog;
    sDialog.setModal(false);
    sDialog.exec();
}

void MainWindow::on_actionInfo_triggered()
{
    InfoDialog iDialog;
    iDialog.setModal(false);
    iDialog.exec();
}
