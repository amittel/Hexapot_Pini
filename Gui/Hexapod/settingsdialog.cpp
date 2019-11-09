#include "settingsdialog.h"
#include "ui_settingsdialog.h"

SettingsDialog::SettingsDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::SettingsDialog)
{
    // Set the Window Icon
    setWindowIcon(QIcon(":/data/files/Decepticons-Logo.png"));
    ui->setupUi(this);
}

SettingsDialog::~SettingsDialog()
{
    delete ui;
}

void SettingsDialog::on_pushButton_4_clicked()
{
    close();
}
