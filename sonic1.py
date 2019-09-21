import retro

#criando o enviroment do gym-retro, ele ta usando o scenario.json
env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')

#dando reset no emulador
env.reset()


#done é variavel que diz se vocẽ perdeu
done = False
while not done:
#mostra a tela do emu, o ideal é não ter isso no treinamento
	env.render()

#recebe uma amostra random dos 12 botões do genesis
#, eles podem tar ligados ou desligados
	#action = env.action_space.sample()
	action = [0,0,1,0,0,0,0,1,1,1,0,0]

#step é o passo, dado por uma ação
#ob é a imagem da tela na hora da ação
#rew é a quantidade que de reward que ele recebeu no cenário
#done é se a condição done foi alcançada ou não
#info é um dicinario de todos os valores setados no data
	ob, rew, done, info = env.step(action)
	print("Action ", action, "Reward ", rew)
	

