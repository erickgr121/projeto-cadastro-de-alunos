from PyQt5 import uic, QtWidgets
import mysql.connector

numero_id = 0

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro1"
)


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()

    turno = ""
    if formulario.radioButton.isChecked():
        print("categoria matutino")
        turno = "matutino"

    elif formulario.radioButton_2.isChecked():
        print("turno vespertino")
        turno = "vespertino"

    print("Nome do aluno:", linha1)
    print("Nome do pai:", linha2)
    print("turma:", linha3, "ªano")
    print("Valor mensalidade:", linha4)

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO formulario2 (aluno,pai,turma,mensalidade,turno) VALUES (%s,%s,%s,%s,%s)"
    VALUES = (str(linha1), str(linha2), str(linha3), str(linha4), turno)
    cursor.execute(comando_SQL, VALUES)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")


def pagamentos():
    nome_do_aluno = pagamento.lineEdit.text()
    janeiro = pagamento.lineEdit_2.text()
    fevereiro = pagamento.lineEdit_3.text()
    marco = pagamento.lineEdit_4.text()
    abril = pagamento.lineEdit_5.text()
    maio = pagamento.lineEdit_6.text()
    junho = pagamento.lineEdit_7.text()
    julho = pagamento.lineEdit_8.text()
    agosto = pagamento.lineEdit_9.text()
    setembro = pagamento.lineEdit_10.text()
    outubro = pagamento.lineEdit_11.text()
    novembro = pagamento.lineEdit_12.text()
    dezembro = pagamento.lineEdit_13.text()
    total = (int(janeiro) + int(fevereiro) + int(marco) + int(abril) + int(maio) + int(junho) + int(julho) + int(agosto)
             + int(setembro) + int(outubro) + int(novembro) + int(dezembro))

    print("nome:", nome_do_aluno)
    print("mensalidade:", janeiro)
    print("mensalidade:", fevereiro)
    print("mensalidade:", marco)
    print("mensalidade:", abril)
    print("mensalidade:", maio)
    print("mensalidade:", junho)
    print("mensalidade:", julho)
    print("mensalidade:", agosto)
    print("mensalidade:", setembro)
    print("mensalidade:", outubro)
    print("mensalidade:", novembro)
    print("mensalidade:", dezembro)
    print(total)

    curso = banco.cursor()
    comando_SQL = "INSERT INTO formulario1 (nome_do_aluno,janeiro,fevereiro,marco,abril,maio, \
                  junho,julho,agosto,setembro,outubro,novembro,dezembro,total) VALUES (%s,%s, \
                  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    VALUES = (
        str(nome_do_aluno), str(janeiro), str(fevereiro), str(marco), str(abril), str(maio), str(junho), str(julho),
        str(agosto), str(setembro), str(outubro), str(novembro), str(dezembro), str(total))

    curso.execute(comando_SQL, VALUES)
    banco.commit()

    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")
    formulario.lineEdit_7.setText("")
    formulario.lineEdit_8.setText("")
    formulario.lineEdit_9.setText("")
    formulario.lineEdit_10.setText("")
    formulario.lineEdit_11.setText("")
    formulario.lineEdit_12.setText("")
    formulario.lineEdit_13.setText("")


def chama_segunda_tela():
    segunda_tela.show()


def dia():
    segunda_tela.show()

    matricula = ""

    if segunda_tela.radioButton.isChecked():
        print("escola escolhido")
        matricula = "escola"

    elif segunda_tela.radioButton_2.isChecked():
        print("integral escolhido")
        matricula = "integral"

    elif segunda_tela.radioButton_3.isChecked():
        print("integral_2 escolhido")
        matricula = "integral_2"

    elif segunda_tela.radioButton_4.isChecked():
        print("integral_3 escolhido")
        matricula = "integral_3"

    elif segunda_tela.radioButton_5.isChecked():
        print("integral_2 + escola escolhido")
        matricula = "integral_2+escola"

    elif segunda_tela.radioButton_6.isChecked():
        print("integral_3 + escola escolhido")
        matricula = "integral_3+escola"

    curso = banco.cursor()
    comando_SQL = "INSERT INTO formulario3 (matricula) VALUES (%s)"
    VALUES = matricula
    curso.execute(comando_SQL, VALUES)


app = QtWidgets.QApplication([])
formulario = uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)
pagamento = uic.loadUi("pagamentos.ui")
pagamento.pushButton.clicked.connect(pagamentos)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela = uic.loadUi("listar_dados.ui")
segunda_tela.pushButton.clicked.connect(dia)

pagamento.show()
formulario.show()
app.exec()
