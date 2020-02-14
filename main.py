import teste
import scripts

# teste.gerarArquivoSVM_LBP()
# teste.gerarArquivoSVM_RH()

#rafael.comparar_labels("labels/labelSVM.txt", "labels/predict_LBP.txt")

# scripts.features_to_svm_train_test("features/rh.txt", 80, 5, 3, 2)

# scripts.ler_predict("./libsvm-3.24/tools/teste.txt.predict", 2)

# scripts.fusao("teste.txt.predict.lbp", "teste.txt.predict.ssd", 80)
# scripts.fusao("teste.txt.predict.lbp", "teste.txt.predict.rh", 80)

scripts.ler_predict("teste.txt.predict.lbp", 2)
scripts.ler_predict("teste.txt.predict.ssd", 2)
scripts.ler_predict("teste.txt.predict.rh", 2)

scripts.ler_predict("predictSoma.txt", 2)
scripts.ler_predict("predictProduto.txt", 2)
scripts.ler_predict("predictMax.txt", 2)
