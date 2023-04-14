from infra.repository.estoque_repo import EstoqueRepo
from infra.repository.fabricante_repo import FabricantesRepo

repo = EstoqueRepo()
resposta = repo.select_one(**{"ID_FABR": 4})
# print(resposta)
for r in resposta:
    print(r.COD_FABR)

# repo2 = FabricantesRepo()
# resp2 = repo2.select_one(22)
# # for r in resp2:
# print(resp2)
