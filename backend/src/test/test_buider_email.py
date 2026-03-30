# # from src.domain.use_case.case_email.buider_email import buider
# # from src.domain.constants.constant_email_send import TEMPLATE_WELCOME
# # Garante que o Python encontre a pasta 'backend' e 'src'

# from src.main.adapter.adapter_email import AdapterEmail
# from src.data.use_case.case_email.use_case_email import UseCaseEmail
# from src.domain.constants.constant_email_send import TEMPLATE_WELCOME



# import sys
# import os


# # def test_buider():
# #     teste = buider(email_class=TEMPLATE_WELCOME)
# #     print(teste)

# sys.path.append(os.path.join(os.getcwd(), "backend"))


# def test_email_send():
#     print("🧪 Iniciando Teste de Integração de E-mail (Hexagonal)")
#     print("-" * 50)

#     try:
#         # 1. Instanciando o Adapter (Lê o .env e prepara o SMTP)
#         print("🔌 Conectando ao Adapter...")
#         adapter = AdapterEmail()

#         # 2. Instanciando o UseCase e injetando o Adapter (D.I.)
#         print("🧠 Montando UseCase com Injeção de Dependência...")
#         email_service = UseCaseEmail(adapter=adapter)

#         # 3. Defina o e-mail de destino (COLOQUE O SEU E-MAIL AQUI)
#         email_destino = "lsantanna.menezes@gmail.com" 

#         print(f"📧 Enviando para: {email_destino}...")

#         # 4. Chama o método de boas-vindas
#         # O UseCase vai chamar o Builder interno e depois o Adapter
#         resultado = email_service.welcome_email(
#             email=email_destino, 
#             email_class=TEMPLATE_WELCOME
#         )

#         if resultado:
#             print("\n✅ SUCESSO! O e-mail foi enviado e aceito pelo servidor SMTP.")
#             print("🚀 Verifique sua caixa de entrada (e a pasta de spam)!")
#         else:
#             print("\n❌ FALHA: O e-mail não foi enviado. Verifique os logs acima.")

#     except Exception as e:
#         print(f"\n💥 ERRO CRÍTICO durante o teste: {e}")
#         print("Dica: Verifique se o seu .env está na pasta correta e se a senha de app está ativa.")

# if __name__ == "__main__":
#     executar_teste()