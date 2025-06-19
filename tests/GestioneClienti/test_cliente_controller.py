import unittest
from unittest.mock import MagicMock, patch

from GestioneClienti.controller.cliente_controller import ClienteController
from GestioneClienti.model.Cliente import Cliente

class ClienteControllerTestCase(unittest.TestCase):
    def setUp(self):

        # Creazione del finto Dao
        patcher = patch(
            'GestioneClienti.daos.ClienteDaoFirebase'
        )
        self.addCleanup(patcher.stop) # pulizia della patch automatica quando finiscono i test
        # oggetto mock che rappresenta il dao
        self.mock_dao_class = patcher.start()
        # l'istanza mock del Dao che il controller utilizzerà (viene creata dinamicamente quando effettivamente viene istanziata)
        self.mock_dao = self.mock_dao_class.return_value

        # Creazione della finta view
        self.view = MagicMock()
        self.view.visualizzaClienti = MagicMock()

        # Inizializzazione del controller
        self.controller = ClienteController(self.view)

    def test_aggiungi_cliente_success(self):
        nuovoCliente = Cliente(
            id='2',
            nome='Mario', 
            cognome='Rossi', 
            sesso= 'Maschio',
            telefono= '3292098383',
            email='mariorossi@esempio.com',
            data_nascita='06/05/2002',
            certificatoMedico=True
            )
        self.mock_dao.aggiungi_cliente.return_value = True

        result = self.controller.aggiungi_cliente(nuovoCliente)

        self.assertTrue(result)
        self.mock_dao.aggiungi_cliente.assert_called_once_with(nuovoCliente)

if __name__ == '__main__':
    unittest.main()

