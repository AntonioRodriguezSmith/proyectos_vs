"""
Utilidad para verificar si Proton VPN está activo.
"""
import subprocess


def vpn_activa() -> bool:
    """Verifica si Proton VPN está corriendo."""
    try:
        result = subprocess.run(
            ['tasklist'], 
            capture_output=True, 
            text=True,
            encoding='utf-8',
            errors='ignore'
        )
        return 'ProtonVPN' in result.stdout
    except Exception:
        return False


def verificar_vpn(advertir: bool = True) -> bool:
    """
    Verifica VPN y muestra aviso si no está activa.
    
    Args:
        advertir: Si True, muestra mensaje de advertencia
        
    Returns:
        True si VPN activa, False si no
    """
    activa = vpn_activa()
    
    if not activa and advertir:
        print("⚠️  AVISO: Proton VPN no está activa")
        print("   Considera activarla para mayor seguridad")
        print()
    
    return activa


if __name__ == "__main__":
    if verificar_vpn():
        print("✅ Proton VPN está activa")
    else:
        print("❌ Proton VPN NO está activa")
