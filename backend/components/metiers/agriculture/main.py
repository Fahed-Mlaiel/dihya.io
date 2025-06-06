# Entrée principale pour le métier Agriculture

def main():
    print("Module Agriculture prêt.")

if __name__ == "__main__":
    import sys
    if '--audit' in sys.argv:
        from audit import audit_agriculture
        print(audit_agriculture())
    else:
        main()
