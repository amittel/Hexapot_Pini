#include "infodialog.h"
#include "ui_infodialog.h"

InfoDialog::InfoDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::InfoDialog)
{
    // Set the Window Icon
    setWindowIcon(QIcon(":/data/files/Decepticons-Logo.png"));
    ui->setupUi(this);
}

InfoDialog::~InfoDialog()
{
    delete ui;
}

void InfoDialog::on_pushButton_clicked()
{
    close();
}
