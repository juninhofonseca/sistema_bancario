
def formatar_moeda(valor):
    return f"R$ {valor:.2f}"

def depositar(saldo, extrato):
    print("\n=== DEPÓSITO ===")
    
    try:
        valor = float(input("Digite o valor a ser depositado: R$ "))
        
        if valor <= 0:
            print("❌ Erro: O valor do depósito deve ser positivo!")
            return saldo, extrato
        
        saldo += valor
        extrato.append(f"Depósito: {formatar_moeda(valor)}")
        
        print(f"✅ Depósito de {formatar_moeda(valor)} realizado com sucesso!")
        print(f"💰 Saldo atual: {formatar_moeda(saldo)}")
        
    except ValueError:
        print("❌ Erro: Digite um valor válido!")
    
    return saldo, extrato

def sacar(saldo, extrato, saques_diarios):
    print("\n=== SAQUE ===")
    
    # Verificar limite de saques diários
    if saques_diarios >= 3:
        print("❌ Erro: Limite de 3 saques diários atingido!")
        return saldo, extrato, saques_diarios
    
    # Verificar se há saldo
    if saldo <= 0:
        print("❌ Erro: Saldo insuficiente para realizar o saque!")
        return saldo, extrato, saques_diarios
    
    try:
        valor = float(input("Digite o valor a ser sacado: R$ "))
        
        if valor <= 0:
            print("❌ Erro: O valor do saque deve ser positivo!")
            return saldo, extrato, saques_diarios
        
        # Verificar limite por saque
        if valor > 500:
            print("❌ Erro: O valor máximo por saque é R$ 500,00!")
            return saldo, extrato, saques_diarios
        
        # Verificar se há saldo suficiente
        if valor > saldo:
            print("❌ Erro: Saldo insuficiente para realizar o saque!")
            return saldo, extrato, saques_diarios
        
        saldo -= valor
        extrato.append(f"Saque: {formatar_moeda(valor)}")
        saques_diarios += 1
        
        print(f"✅ Saque de {formatar_moeda(valor)} realizado com sucesso!")
        print(f"💰 Saldo atual: {formatar_moeda(saldo)}")
        print(f"📊 Saques restantes hoje: {3 - saques_diarios}")
        
    except ValueError:
        print("❌ Erro: Digite um valor válido!")
    
    return saldo, extrato, saques_diarios

def exibir_extrato(saldo, extrato):
    print("\n" + "="*50)
    print("🏦 EXTRATO BANCÁRIO")
    print("="*50)
    
    if not extrato:
        print("📝 Não foram realizadas movimentações.")
    else:
        print("📋 Histórico de movimentações:")
        for i, movimentacao in enumerate(extrato, 1):
            print(f"  {i}. {movimentacao}")
    
    print("-" * 50)
    print(f"💰 Saldo atual: {formatar_moeda(saldo)}")
    print("="*50)

def exibir_menu():
    print("\n" + "="*50)
    print("🏦 SISTEMA BANCÁRIO v1.0")
    print("="*50)
    print("Escolha uma opção:")
    print("1. 💰 Depositar")
    print("2. 💸 Sacar")
    print("3. 📋 Extrato")
    print("4. 🚪 Sair")
    print("-" * 50)

def main():
    saldo = 0.0
    extrato = []
    saques_diarios = 0
    
    print("🎉 Bem-vindo ao Sistema Bancário!")
    print("💡 Dica: Você pode realizar até 3 saques por dia, com limite de R$ 500,00 por saque.")
    
    while True:
        exibir_menu()
        
        try:
            opcao = input("Digite sua opção: ").strip()
            
            if opcao == "1":
                saldo, extrato = depositar(saldo, extrato)
                
            elif opcao == "2":
                saldo, extrato, saques_diarios = sacar(saldo, extrato, saques_diarios)
                
            elif opcao == "3":
                exibir_extrato(saldo, extrato)
                
            elif opcao == "4":
                print("\n👋 Obrigado por usar nosso sistema bancário!")
                print("💳 Volte sempre!")
                break
                
            else:
                print("❌ Opção inválida! Digite um número de 1 a 4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Sistema interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
