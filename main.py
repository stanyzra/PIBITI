import teste
import scripts

# teste.gerarArquivoSVM_LBP()
# teste.gerarArquivoSVM_RH()

#rafael.comparar_labels("labels/labelSVM.txt", "labels/predict_LBP.txt")

scripts.features_to_svm("features/lbp.txt", 59, 80, 5, 3, 2)
