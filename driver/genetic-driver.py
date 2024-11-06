import algorithm.gene as gene

if __name__ == "__main__":
    search = gene.GeneticAlgorithm()
    cube_instance, objective_value = search.genetic_search(10)

    cube_instance.display_cube()
    print("Nilai fungsi objektif:", objective_value)