package Maqest;

public class MaquinaEstados<EV>{

	private Estado<EV> estado;
	
	public MaquinaEstados(Estado<EV> estado){
		this.estado = estado;
	}
	
	//getter do estado
	public Estado<EV> getEstado(){
		return this.estado;
	}
	
	public void processarEvento(EV evento){
		///atualiza o estado atual da maquina de estado sempre que é aplicada uma nova acção implicando 
		//um novo estado, sendo esse igual ao atual ou diferente
		Estado<EV> novoEstado = estado.processar(evento);
		if(novoEstado != null){
			estado = novoEstado;
		}
	}
}
